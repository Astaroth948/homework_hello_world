# Парсер log файлов

Формат файла должен быть:
```109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" 4374```

Запуск анализа одного файла:
```python homework_9\log_parser.py --file="c:\code\111\access.log"```

Запуск анализа всех файлов из директории:
```python homework_9\log_parser.py --directory c:\code\111\222\```

Вывод информации в консоль (по умолчанию одключено):
```python homework_9\log_parser.py --file="c:\code\111\access.log" --verbose```

Сохранение результатов происходит в папку results в файл в формате json.
