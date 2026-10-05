from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def msg():
    return {"message": "hello"}


@app.get("/health")
def health():
    return {"status": "ok"}
