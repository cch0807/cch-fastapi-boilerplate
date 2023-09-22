from fastapi import FastAPI


app = FastAPI(version="0.1.0")


@app.get("/")
def health_check_handler():
    return {"ping": "pong"}
