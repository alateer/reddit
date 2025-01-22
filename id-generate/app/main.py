from fastapi import FastAPI
from .api import id_generate

app = FastAPI()

app.include_router(id_generate.router)

@app.get("/")
async def root():
    return { "message": "hello Bigger Applications!" }