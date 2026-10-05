# Основы HTTP

## Клиент и сервер

Клиент отправляет HTTP-запрос.

Сервер принимает запрос, обрабатывает его и отправляет HTTP-ответ.

Схема:

Client → HTTP request → Server  
Client ← HTTP response ← Server

В моем будущем проекте:

- клиент — браузер или frontend
- сервер — FastAPI-приложение, запущенное на моем компьютере

---

## HTTP-запрос

HTTP-запрос может содержать:

- метод
- path
- query-параметры
- headers
- body

Пример:

POST /predict?debug=true
Content-Type: application/json
Accept: application/json

{
  "text": "hello"
}

Здесь:

- `POST` — HTTP-метод
- `/predict` — path
- `debug=true` — query-параметр
- `Content-Type` и `Accept` — headers
- `{ "text": "hello" }` — request body

---

## HTTP-методы

Основные методы:

- `GET` — получить данные
- `POST` — отправить данные, создать ресурс или запустить обработку
- `PUT` — полностью заменить ресурс
- `PATCH` — частично изменить ресурс
- `DELETE` — удалить ресурс

Примеры:

GET /users  
GET /users/42  
POST /users  
POST /predict

---

## Path, query и body

### Path

Path указывает, к какому ресурсу мы обращаемся.

Пример:

GET /users/42

Здесь `/users/42` — path.

---

### Query parameters

Query-параметры обычно используются для фильтрации, сортировки или дополнительных настроек запроса.

Пример:

GET /users?active=true&limit=10

Здесь:

- `active=true`
- `limit=10`

— query-параметры.

---

### Body

Body содержит данные, которые клиент отправляет серверу.

Пример:

{
  "text": "hello"
}

Для больших данных или данных для обработки обычно используется body.

---

## Headers

Headers содержат дополнительную информацию о запросе или ответе.

Примеры:

`Content-Type: application/json`

означает, что body записан в формате JSON.

`Accept: application/json`

означает, что клиент хочет получить ответ в формате JSON.

`Authorization: Bearer ...`

содержит данные для авторизации.

---

## JSON

JSON — один из основных форматов передачи данных в API.

Пример:

{
  "text": "hello",
  "age": 25,
  "active": true,
  "tags": ["ml", "python"]
}

Соответствие JSON и Python:

- string → `str`
- number → `int` / `float`
- boolean → `bool`
- array → `list`
- object → `dict`
- null → `None`

---

## HTTP-ответ

HTTP-ответ обычно содержит:

- status code
- headers
- body

Пример:

HTTP/1.1 200 OK
Content-Type: application/json

{
  "prediction": "positive"
}

Здесь:

- `200 OK` — status code
- `Content-Type` — response header
- `{ "prediction": "positive" }` — response body

---

## Status codes

Основные коды, которые нужно знать:

- `200 OK` — запрос успешно обработан
- `201 Created` — ресурс успешно создан
- `400 Bad Request` — запрос сформирован некорректно
- `401 Unauthorized` — пользователь не авторизован или credentials неверные
- `403 Forbidden` — пользователь известен, но у него нет прав
- `404 Not Found` — ресурс не найден
- `422 Unprocessable Entity` — данные не прошли валидацию
- `500 Internal Server Error` — ошибка внутри сервера

Примеры:

Если пользователя с id `999` не существует:

404 Not Found

Если сервер ожидает число, а клиент отправляет строку:

422 Unprocessable Entity

Если внутри Python-кода произошла необработанная ошибка:

500 Internal Server Error

---

## HTTP и HTTPS

HTTP передает данные без шифрования.

HTTPS — это HTTP поверх TLS, поэтому данные между клиентом и сервером шифруются.

Логика request/response при этом остается той же.

Стандартные порты:

- HTTP → `80`
- HTTPS → `443`

---

## Структура URL

Пример:

http://localhost:8000/users/42?active=true

Здесь:

- `http` — protocol
- `localhost` — host
- `8000` — port
- `/users/42` — path
- `active=true` — query-параметр

`localhost` означает текущий компьютер.

Port нужен, чтобы операционная система понимала, какой программе передать запрос.

Например:

localhost:8000 → FastAPI  
localhost:5432 → PostgreSQL

---

## Что я теперь понимаю

Я понимаю общий путь HTTP-запроса:

Client  
↓  
HTTP request  
↓  
Server  
↓  
Processing  
↓  
HTTP response  
↓  
Client

Я понимаю разницу между:

- method
- path
- query parameters
- headers
- body
- status code

Следующий этап — FastAPI.
