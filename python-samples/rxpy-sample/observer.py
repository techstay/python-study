from rx import of, operators as op
import rx

ob = of(1, 2, 34, 5, 6, 7, 7)
subscription = ob.pipe(
    op.map(lambda i: i ** 2),
    op.filter(lambda i: i >= 10)
).subscribe(lambda i: print(f'Received: {i}'))


def capitalize():
    return op.pipe(
        op.map(lambda i: i.capitalize())
    )


of('ab', 'cd', 'efg').pipe(capitalize()).subscribe(lambda i: print(f'Received: {i}'))
