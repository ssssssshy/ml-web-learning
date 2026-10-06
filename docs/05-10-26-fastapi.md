# FastAPI

## Что изучил

### Создание FastAPI приложения

```python
from fastapi import FastAPI

app = FastAPI()
```

`FastAPI()` создаёт приложение, которое принимает HTTP-запросы.

---

## GET запросы

Создал два endpoint:

- `GET /`
- `GET /health`

Пример:

```python
@app.get("/")
def msg():
    return {"message": "hello"}


@app.get("/health")
def health():
    return {"status": "ok"}
```

FastAPI автоматически преобразует Python `dict` в JSON.

Например:

```python
return {"status": "ok"}
```

клиент получает как:

```json
{
  "status": "ok"
}
```

---

## POST запрос

Создал endpoint:

```text
POST /predict
```

Он принимает данные от клиента через request body.

Пример запроса:

```json
{
  "text": "hello"
}
```

Пример endpoint:

```python
@app.post("/predict")
def predict(request: PredictionRequest):
    return {"prediction": "positive"}
```

Ответ:

```json
{
  "prediction": "positive"
}
```

---

## Pydantic

Для описания структуры входных данных используется `BaseModel`:

```python
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    text: str
```

Эта модель говорит FastAPI, что request body должен содержать:

```json
{
  "text": "строка"
}
```

После валидации данные доступны как Python-объект:

```python
request.text
```

---

## Валидация

FastAPI вместе с Pydantic автоматически проверяет входные данные.

Правильный запрос:

```json
{
  "text": "hello"
}
```

вернёт:

```text
200 OK
```

Если обязательного поля нет:

```json
{}
```

FastAPI вернёт:

```text
422 Unprocessable Entity
```

Если тип данных неправильный, например:

```json
{
  "text": 123
}
```

валидация также не пропустит запрос.

---

## Как проходит POST запрос

```text
Клиент
  ↓
POST /predict
  ↓
JSON body
  ↓
PredictionRequest
  ↓
Pydantic validation
  ↓
Python функция predict()
  ↓
Python dict
  ↓
JSON response
```

---

## Запуск приложения

Приложение можно запустить:

```bash
uv run fastapi dev src/main.py
```

После запуска:

```text
http://127.0.0.1:8000
```

Swagger документация:

```text
http://127.0.0.1:8000/docs
```

Через `/docs` можно вручную отправлять запросы к API и смотреть ответы.

---

## Что изучить дальше

- Response Model
- Path Parameters
- Query Parameters
- Обработка ошибок
