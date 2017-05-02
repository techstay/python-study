# Q1
from datetime import date

now = date.today()
now_string = now.isoformat()

with open('today.txt', 'w') as file:
    print(now, file=file)

# Q2
today_string = None
with open('today.txt') as file:
    today_string = file.read()

print(today_string)

# Q3
from datetime import datetime

format = '%Y-%m-%d\n'
print(datetime.strptime(today_string, format))

# Q4
import os

print(os.listdir('.'))

# Q5
print(os.listdir('..'))

# Q6
import multiprocessing


def print_current_time(seconds):
    from time import sleep
    sleep(seconds)
    print(f'Wait for {seconds} seconds, Current time is {datetime.today().time()}')


import random

# 由于Windows下multiprocess会执行整个代码块，所以会引起循环创建进程的问题
# 这需要下面的代码来避免
if __name__ == '__main__':
    for n in range(3):
        seconds = random.random()
        process = multiprocessing.Process(target=print_current_time, args=(seconds,))
        process.start()

# Q7

my_birthday = date(1993, 8, 13)
print(my_birthday)

# Q8
# 星期从零开始计数
print(my_birthday.weekday())
# 星期从一开始计数
print(my_birthday.isoweekday())

# Q9
from datetime import timedelta

ten_thousand_day_after_my_birthday = my_birthday + timedelta(days=10000)
print(ten_thousand_day_after_my_birthday)
