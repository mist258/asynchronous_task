from fastapi import FastAPI
import time
import asyncio

"""
time.sleep() — блокує весь event loop, інші запити чекають
await asyncio.sleep() — повертає контроль event loop, дозволяє обробляти інші запити
Тобто, в блокуючому коді послідовне виконання запитів (1 запит за раз);
в асинхронному коді паралельна обробка (кілька запитів одночасно)
"""

app = FastAPI()

@app.get("/blocking")
def blocking():
    time.sleep(2)
    return {"Details": "blocking done"}

@app.get("/non_blocking")
async def non_blocking():
    await asyncio.sleep(2)
    return {"Details": "non_blocking done"}


