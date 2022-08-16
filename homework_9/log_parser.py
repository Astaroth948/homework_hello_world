from argparse import ArgumentParser
import json
import os.path
import re
from datetime import datetime
from pprint import pprint

RE_METHODS = r'(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE|PATCH)'
RE_IP_ADDRESS = r'(\d{1,3}\.){3}\d{1,3}'
RE_URL = r'"(http[s]?:\/\/.+)" "'
RE_DATE_TIME = r'\[(.+) \+\d{4}\]'
RE_DURATION = r'\d+$'


def arg_parser(parser: ArgumentParser) -> list:
    parser.add_argument('--file', dest='path_to_logfile',
                        action='store', help='Путь к log файлу')
    parser.add_argument('--directory', dest='path_to_directory',
                        action='store', help='Путь к директории с log файлами')
    parser.add_argument('--verbose', dest='verbose', action='store_true', default=False,
                        help='Показывать ход выполнения работы скрипта в stdout')
    return parser.parse_args()


def get_log_files(args) -> list:
    log_files = []

    if args.path_to_logfile:
        log_files.append(args.path_to_logfile)
    else:
        files = os.listdir(args.path_to_directory)
        for item in files:
            if item.endswith(".log"):
                log_files.append(
                    str(os.path.join(args.path_to_directory, item)))

    return log_files


def open_logfile(path_to_logfile: str) -> list:
    logfile = []
    with open(path_to_logfile, "r") as log:
        for line in log:
            logfile.append(line)
    return logfile


def convert_logfile(logfile: list) -> list:
    logfile_list = []

    for line in logfile:
        logfile_dict = {}
        method = re.search(RE_METHODS, line)
        url = re.search(RE_URL, line)
        ip = re.search(RE_IP_ADDRESS, line)
        duration = re.search(RE_DURATION, line)
        date_time = re.search(RE_DATE_TIME, line)

        logfile_dict.update({'method': method.group(0) if method else '-'})
        logfile_dict.update({'url': url.group(0) if url else '-'})
        logfile_dict.update({'ip': ip.group(0) if ip else '-'})
        logfile_dict.update(
            {'duration': int(duration.group(0)) if duration else 0})
        logfile_dict.update(
            {'date_time': date_time.group(0) if date_time else '-'})

        logfile_list.append(logfile_dict)

    return logfile_list


def get_quantity_requests_by_methods(logfile_list: list) -> dict:
    requests_dict = {
        "GET": 0,
        "HEAD": 0,
        "POST": 0,
        "PUT": 0,
        "DELETE": 0,
        "CONNECT": 0,
        "OPTIONS": 0,
        "TRACE": 0,
        "PATCH": 0
    }

    for line in logfile_list:
        if line['method'] != '-':
            requests_dict.update(
                {line['method']: requests_dict[line['method']] + 1})

    return requests_dict


def get_top_3_duration_requests(logfile_list: list) -> dict:
    return sorted(logfile_list, key=lambda x: x['duration'], reverse=True)[0:3]


def get_most_requests_quantity_ip(logfile_list: list) -> list:
    ip_dict = {}
    for line in logfile_list:
        if line['ip'] != '-':
            if line['ip'] not in ip_dict.keys():
                ip_dict.update({line['ip']: 1})
            else:
                ip_dict.update({line['ip']: ip_dict[line['ip']] + 1})

    return sorted(ip_dict, key=ip_dict.get, reverse=True)[0:3]


def generate_report(file_name: str, total_requests: int, quantity_requests: dict, top_ip: list, top_duration: list) -> list:
    report = [
        {'Файл': file_name},
        {'Количество запросов': total_requests},
        {'Количество запросов по HTTP-методам': quantity_requests},
        {'Топ 3 IP адресов по количеству запросов': top_ip},
        {'Топ 3 самых долгих запросов': top_duration},
    ]

    return report


def save_report(report: list) -> None:
    current_date = datetime.now().strftime('%d-%m-%Y-%H-%M-%S%f')
    with open(f'homework_9/results/result-{current_date}.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)


def print_report(report: list) -> None:
    print(f'''Отчет по файлу: {report[0]['Файл']}
Количество запросов: {report[1]['Количество запросов']}
Количество запросов по HTTP-методам: ''')
    pprint(report[2]['Количество запросов по HTTP-методам'])
    print(f'''Топ 3 IP адресов по количеству запросов: {report[3]['Топ 3 IP адресов по количеству запросов']}
Топ 3 самых долгих запросов: ''')
    pprint(report[4]['Топ 3 самых долгих запросов'])


if __name__ == '__main__':
    args = arg_parser(parser=ArgumentParser())
    logfiles = get_log_files(args=args)
    for file in logfiles:
        if args.verbose:
            print(f'\nАнализ {file}\n')
        logfile = open_logfile(path_to_logfile=file)
        if args.verbose:
            print(
                '\\__ Подсчет общего количества запросов')
        total_requests = len(logfile)
        logfile_list = convert_logfile(logfile)
        if args.verbose:
            print('\\__ Подсчет запросов по методам ')
        quantity_requests = get_quantity_requests_by_methods(logfile_list)
        if args.verbose:
            print('\\__ Поиск самых частых IP адресов ')
        top_ip = get_most_requests_quantity_ip(logfile_list)
        if args.verbose:
            print('\\__ Поиск самых долгих запросов ')
        top_duration = get_top_3_duration_requests(logfile_list)
        if args.verbose:
            print('\\__ Генерация отчета\n')
        report = generate_report(file_name=file, total_requests=total_requests,
                                 quantity_requests=quantity_requests, top_duration=top_duration, top_ip=top_ip)
        save_report(report=report)
        if args.verbose:
            print_report(report=report)
