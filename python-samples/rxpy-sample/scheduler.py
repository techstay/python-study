import rx
from rx.scheduler import ThreadPoolScheduler
from rx import operators as op

import multiprocessing
import time
import threading
import random


def long_work(value):
    time.sleep(random.randint(5, 20) / 10)
    return value


pool_schedular = ThreadPoolScheduler(multiprocessing.cpu_count())

rx.range(5).pipe(
    op.map(lambda i: long_work(i + 1)),
    op.subscribe_on(pool_schedular)
).subscribe(lambda i: print(f'Work 1: {threading.current_thread().name}, {i}'))

rx.of(1, 2, 3, 4, 5).pipe(
    op.map(lambda i: i * 2),
    op.subscribe_on(pool_schedular)
).subscribe(lambda i: print(f'Work 2: {threading.current_thread().name}, {i}'))
