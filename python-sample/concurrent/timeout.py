import asyncio


async def very_long_work():
    await asyncio.sleep(3600)
    print("SOOOOOOOOOOO LONG")


async def main():
    try:
        await asyncio.wait_for(very_long_work(), timeout=2)

    except TimeoutError:
        print("Timeout!")


asyncio.run(main())
