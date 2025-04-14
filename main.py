import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def funcaoteste():
    print("função foi chamada")
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}
