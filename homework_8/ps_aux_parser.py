from datetime import datetime
from subprocess import (run, PIPE)


def get_ps_aux_results() -> str:
    result = run(["ps", "aux"], stderr=PIPE, stdout=PIPE)
    return result.stdout.decode("utf-8").split("\n")[1:-1]


def convert_result(ps_aux_results: list) -> list:
    ps_aux_results_list = []
    values_list = []

    for ps_aux_row in ps_aux_results:
        ps_aux_dict = {}
        values_list = ps_aux_row.split(maxsplit=10)
        if len(values_list) == 10:
            values_list.append('')
        ps_aux_dict.update(
            {
                'USER': values_list[0],
                'PID': int(values_list[1]),
                '%CPU': float(values_list[2]),
                '%MEM': float(values_list[3]),
                'VSZ': int(values_list[4]),
                'RSS': int(values_list[5]),
                'TTY': values_list[6],
                'STAT': values_list[7],
                'START': values_list[8],
                'TIME': values_list[9],
                'COMMAND': values_list[10],
            })

        ps_aux_results_list.append(ps_aux_dict)

    return ps_aux_results_list


def get_users(ps_aux_results_list: list) -> list:
    users_list = []
    for row in ps_aux_results_list:
        if row['USER'] not in users_list:
            users_list.append(row['USER'])

    return users_list


def users_processes(ps_aux_results_list: list, users_list: list) -> dict:
    users_dict = {}
    for user in users_list:
        processes_count = 0
        for row in ps_aux_results_list:
            if user == row['USER']:
                processes_count += 1
        users_dict.update({user: processes_count})

    return users_dict


def get_total_processes(ps_aux_results_list: list) -> int:
    return len(ps_aux_results_list)


def get_total_memory(ps_aux_results_list: list) -> float:
    total_memory = 0
    for row in ps_aux_results_list:
        total_memory += row['%MEM']

    return format(total_memory, '.1f')


def get_total_cpu(ps_aux_results_list: list) -> float:
    total_cpu = 0
    for row in ps_aux_results_list:
        total_cpu += row['%CPU']

    return format(total_cpu, '.1f')


def get_max_memory(ps_aux_results_list: list) -> list:
    return format(sorted(ps_aux_results_list, key=lambda x: x['%MEM'])[-1]['COMMAND'], '.20s')


def get_max_cpu(ps_aux_results_list: list) -> list:
    return format(sorted(ps_aux_results_list, key=lambda x: x['%CPU'])[-1]['COMMAND'], '.20s')


def generate_report() -> str:
    ps_aux_results = get_ps_aux_results()
    ps_aux_results_list = convert_result(ps_aux_results)
    total_processes = get_total_processes(ps_aux_results_list)
    users_list = get_users(ps_aux_results_list)
    users_str = "','".join(users_list)
    users_processes_dict = users_processes(ps_aux_results_list, users_list)
    users_processes_str = ''
    total_memory = get_total_memory(ps_aux_results_list)
    total_cpu = get_total_cpu(ps_aux_results_list)
    max_memory = get_max_memory(ps_aux_results_list)
    max_cpu = get_max_cpu(ps_aux_results_list)

    for user in sorted(users_processes_dict, key=users_processes_dict.get, reverse=True):
        users_processes_str += f'\n {user}: {users_processes_dict[user]}'

    report = f'''Отчет о состоянии системы:
Пользователи системы: '{users_str}'
Процессов запущено: {total_processes}
Пользовательских процессов: {users_processes_str}
Всего памяти используется: {total_memory} mb
Всего CPU используется: {total_cpu}%
Больше всего памяти использует: {max_memory}
Больше всего CPU использует: {max_cpu}
'''

    return report


def save_report(report: str) -> None:
    current_date = datetime.now().strftime('%d-%m-%Y-%H-%M')
    with open(f'{current_date}-scan.txt', 'w') as f:
        f.write(report)


if __name__ == '__main__':
    report = generate_report()
    print(report)
    save_report(report)
