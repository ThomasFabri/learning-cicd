import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste():
    print("função foi chamada")
    return {"teste": "deu certo", "num_aleatorio": random.randint(0, 10000)}