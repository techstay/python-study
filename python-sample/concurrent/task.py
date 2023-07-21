import asyncio
import time


async def task1():
    await asyncio.sleep(1)
    return "foo"


async def task2():
    await asyncio.sleep(1.5)
    return "bar"


async def serialize_tasks():
    t1 = time.time()
    s1 = await task1()
    s2 = await task2()
    t2 = time.time()

    print(s1, s2)
    print(f"time used: {t2-t1:.3f} secs")


async def parallel_tasks():
    s1 = None
    s2 = None
    t1 = None
    async with asyncio.TaskGroup() as tg:
        s1 = tg.create_task(task1())
        s2 = tg.create_task(task2())
        t1 = time.time()
    t2 = time.time()
    print(s1.result(), s2.result())
    print(f"time used: {t2-t1:.3f} secs")


if __name__ == "__main__":
    asyncio.run(serialize_tasks())
    asyncio.run(parallel_tasks())
