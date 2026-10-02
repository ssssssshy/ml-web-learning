# HTTP

## What I understood

Browser is an HTTP client.

FastAPI application runs an HTTP server.

When browser sends:

POST /predict

the request contains:
- method
- URL
- headers
- body

FastAPI receives the request and selects
the Python function associated with /predict.

The function returns Python data.

FastAPI serializes it to JSON and sends
an HTTP response.

## Things I still don't understand

- What exactly is TCP?
- Why do we need ports?
- What does CORS do?