import asyncio
import aiohttp
import time


async def test(url, name):
    print(f"{name}")
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for _ in range(5)]
        response = await asyncio.gather(*tasks)
        for resp in response:
            await resp.json()

    duration = time.time() - start
    print(f"Time: {duration:.2f}s")
    return duration

async def main():

    time1 = await test("http://localhost:8000/blocking", "BLOCKING")
    time2 = await test("http://localhost:8000/npn-blocking", "NON-BLOCKING")

    print("\n" + "*" * 50)
    print(f"Blocking:     {time1:.2f}s")
    print(f"Non-blocking: {time2:.2f}s")
    print(f"Difference:   {time1 - time2:.2f}s")
    print("*" * 50)


if __name__ == "__main__":
    asyncio.run(main())





