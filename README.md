### Приложение "Книжная лавка"

Небольшое приложение с наглядными интеграциями с Jaeger/Sentry/ELK

## Запускаем

1: внешние сервисы
 - регистрируем аккаунт для ELK https://cloud.elastic.co/login?redirectTo=%2Fhome
 - добавляем авторизационные метаданные в ./filebeat.yml
 - регистрируем аккаунт для Sentry https://sentry.io/auth/login/
 - добавляем авторизационные метаданные в ./lib/settings.py

2: конфигурируем базы данных
```shell script
make migrate
```

3: запускаем
```shell script
make up
```

## Note

Интерфейс Jaeger если используем сконфигурированный в этом проекте - http://localhost:16686/