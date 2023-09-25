from fastapi import FastAPI


app = FastAPI(
    title="Infrastruct",
    version="0.1.0",
    summary="Megastudy & Mais Infrastruct template",
)


@app.get("/")
async def health_check_handler():
    return {"ping": "pong"}
