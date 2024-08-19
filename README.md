# test_o_complex

## Используемые технологии

FastApi, SQLalchemy, SQLLite.
Все зависимости находятся в файле requirements.txt.

## Принцип работы

### Сохранение пользователей

Api также сохраняет пользователей при помощи cookie. Когда пользователь заходит на главную страницу, js скрипт отправляет запрос на сервер для генерации уникального идентификатора пользователя (user_id), после чего устанавливает этот идентификатор в cookie. Когда пользователь выполняет запрос для получения данных о погоде, сервер сохраняет его запрос в базе данных с его идентификатором.

### Процесс получения данных

Пользователь вводит название города, сервисная часть приложения находит координаты этого места и выдает данные о погоде на данный момент.
Api сохраняет в бд место, которое искал пользователь и обновляет количество запросов по этому месту (или создает новую запись с счетчиком равным единице), после чего выводит данные о погоде.
