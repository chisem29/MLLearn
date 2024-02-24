import asyncio
import time 

async def nested():
    time.sleep(1)
    return 42

print(asyncio.run(nested()))

async def name(time, name) :
    await asyncio.sleep(time)
    print(name)

async def main() :
    task1 = asyncio.create_task(
        name(2, 'hello'))

    task2 = asyncio.create_task(
        name(3, 'world'))
    print("sosi", await nested())
    await task1
    await task2

asyncio.run(main())
