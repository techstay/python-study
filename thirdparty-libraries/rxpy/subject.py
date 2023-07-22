# %%
from reactivex.subject import AsyncSubject, BehaviorSubject, ReplaySubject, Subject

# Subject同时是Observer和Observable

subject = Subject()
subject.on_next(1)
subject.subscribe(lambda i: print(i))
subject.on_next(2)
subject.on_next(3)
subject.on_next(4)
subject.on_completed()
# %%

# ReplaySubject会缓存所有值，如果指定参数的话只会缓存最近的几个值
subject = ReplaySubject()
subject.on_next(1)
subject.subscribe(lambda i: print(i))
subject.on_next(2)
subject.on_next(3)
subject.on_next(4)
subject.on_completed()

# %%

# BehaviorSubject会缓存上次发射的值，除非Observable已经关闭
subject = BehaviorSubject(0)
subject.on_next(1)
subject.on_next(2)
subject.subscribe(lambda i: print(i))
subject.on_next(3)
subject.on_next(4)
subject.on_completed()
# %%
# AsyncSubject会缓存上次发射的值，而且仅会在Observable关闭后开始发射
subject = AsyncSubject()
subject.on_next(1)
subject.on_next(2)
subject.subscribe(lambda i: print(i))
subject.on_next(3)
subject.on_next(4)
subject.on_completed()

# %%
