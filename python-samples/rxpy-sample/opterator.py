import rx
from rx import operators as op
from rx.subject import Subject
import datetime

print('1-100求和')
rx.range(1, 101).pipe(
    op.reduce(lambda acc, i: acc + i, 0)
).subscribe(lambda i: print(i))

# 操作数据流
print('求所有偶数')
some_data = rx.of(1, 2, 3, 4, 5, 6, 7, 8)
some_data2 = rx.from_iterable(range(10, 20))
some_data.pipe(
    op.merge(some_data2),
    op.filter(lambda i: i % 2 == 0),
    # op.map(lambda i: i * 2)
).subscribe(lambda i: print(i))

# debounce操作符，仅在时间间隔之外的可以发射
print('防止重复发送')
ob = Subject()
ob.pipe(
    op.throttle_first(3)
    # op.debounce(3)
).subscribe(
    on_next=lambda i: print(i),
    on_completed=lambda: print('Completed')
)

print('press enter to print, press other key to exit')
while True:
    s = input()
    if s == '':
        ob.on_next(datetime.datetime.now().time())
    else:
        ob.on_completed()
        break
