import asyncio
import aiohttp
import requests
import time
from multiprocessing import Pool

URL = "https://httpbin.org/delay/2"

# asynchronous variant
async def async_request():
    print(f"ASYNCHRONOUS")
    start = time.time()

    async with aiohttp.ClientSession() as session:
        task = []
        for i in range(1,6):
            task.append(session.get(URL))

        response = await asyncio.gather(*task)

        for i, res in enumerate(response, 1):
            await res.json()
            print(f"Request: {i}")
    finish = time.time()
    print(f"{finish - start:.2f}  seconds\n")
    return finish - start


# synchronous variant
def sync_request():
    print("SYNCHRONOUS")
    start = time.time()

    for i in range(1,6):
        requests.get(URL)
        print(f"Request: {i}")

    finish = time.time()
    print(f"{finish - start:.2f}  seconds\n")
    return finish - start


# multiprocessing variant
def request(numb):
    requests.get(URL)
    print(f"Request: {numb}")

def run_multiprocessing():
    print("MULTIPROCESSING")

    start = time.time()

    with Pool(5) as pool:
        pool.map(request, range(1,6))

    finish = time.time()
    print(f"{finish - start:.2f}  seconds\n")
    return finish - start


if __name__ == "__main__":
    print("=" * 50)

    time_async = asyncio.run(async_request())
    time_sync = sync_request()
    time_multi = run_multiprocessing()

    print("=" * 50)
    print("RESULT:")
    #print("=" * 50)
    print(f"Asynchronous:    {time_async:.2f} seconds")
    print(f"Synchronous:     {time_sync:.2f} seconds")
    print(f"Multiprocessing: {time_multi:.2f} seconds")
    print("=" * 50)





