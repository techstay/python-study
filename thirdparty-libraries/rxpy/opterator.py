import reactivex
from reactivex import operators as op

# %%
# sum of 1-100
reactivex.range(1, 101).pipe(op.reduce(lambda acc, i: acc + i, 0)).subscribe(
    lambda i: print(i)
)
# %%
# 操作数据流

# 求所有偶数
some_data = reactivex.of(1, 2, 3, 4, 5, 6, 7, 8)
some_data2 = reactivex.from_iterable(range(10, 20))
some_data.pipe(
    op.merge(some_data2),
    op.filter(lambda i: i % 2 == 0),
    # op.map(lambda i: i * 2)
).subscribe(lambda i: print(i))

# %%
