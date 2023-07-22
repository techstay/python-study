import datetime

from reactivex import Subject
from reactivex import operators as op

# debounce操作符，仅在时间间隔之外的可以发射

ob = Subject()
ob.pipe(
    op.throttle_first(0.1),
    op.debounce(1),
).subscribe(on_next=lambda i: print(i), on_completed=lambda: print("Completed"))

print("press enter to print, press other key to exit")
while True:
    s = input()
    if s == "":
        ob.on_next(datetime.datetime.now().time())
    else:
        ob.on_completed()
        break
