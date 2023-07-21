import asyncio


async def task1():
    await asyncio.sleep(2)
    return 42


async def main():
    print("before task1")
    rst = await task1()
    print(rst)


asyncio.run(main())
