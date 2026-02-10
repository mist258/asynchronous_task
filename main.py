from fastapi import FastAPI
import time
import asyncio


app = FastAPI()

@app.get("/blocking")
def blocking():
    time.sleep(2)
    return {"Details": "blocking done"}

@app.get("/non_blocking")
async def non_blocking():
    await asyncio.sleep(2)
    return {"Details": "non_blocking done"}

