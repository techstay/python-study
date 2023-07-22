# %%

import multiprocessing
import random
import threading
import time

import reactivex
from reactivex import operators as op
from reactivex.scheduler import ThreadPoolScheduler


def long_work(value):
    time.sleep(random.randint(5, 20) / 10)
    return value


pool_schedular = ThreadPoolScheduler(multiprocessing.cpu_count())

reactivex.range(5).pipe(
    op.map(lambda i: long_work(i + 1)), op.subscribe_on(pool_schedular)
).subscribe(lambda i: print(f"Work 1: {threading.current_thread().name}, {i}"))

# %%
reactivex.of(1, 2, 3, 4, 5).pipe(
    op.map(lambda i: i * 2), op.subscribe_on(pool_schedular)
).subscribe(lambda i: print(f"Work 2: {threading.current_thread().name}, {i}"))

# %%
