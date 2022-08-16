# Домашние работы по курсу OTUS

## Запуск тестов в Docker

Запуск контейнера

```
docker build -t tests . -f Dockerfile
docker run --name tests_run --network selenoid tests homework_7/tests/ -s --url=http://192.168.0.102:8081/ --headless --executor=192.168.0.102
```

Копирование отчетов Allure из контейнера

```
docker cp tests_run:app/homework_7/allure_results homework_7/
```

Удаление контейнера

```
docker rm tests_run
```
