# %%
def foo():
    print("foo function")


foo()


# %%
def bar(a, b):
    print(f"a:{a}, b:{b}")


bar(1, 2)
bar(3, 4)

# call functions using keyword arguments
bar(a=22, b=33)
bar(b=22, a=33)


# %%
def fun_with_default_param(n=1000):
    print(f"n={n}")


fun_with_default_param()
fun_with_default_param(5)


# %%
def fun_with_varargs(*args):
    # treated as a list inside the function
    for arg in args:
        print(arg, end=", ")
    print()


fun_with_varargs(1, 2)
fun_with_varargs(1, 2, 3, 4)

# unpacking arguments
fun_with_varargs(*"abcd")


# %%
def fun_with_keyword_args(**kargs):
    print("received arguments:")
    for k, v in kargs.items():
        print(f"{k}={v}", end=", ")
    print()


fun_with_keyword_args(a=1)
fun_with_keyword_args(a=1, b=2)
fun_with_keyword_args(foo="abc", bar="xyz", x=100)

kargs = {"name": "jack", "age": 18, "gender": "male"}
fun_with_keyword_args(**kargs)


# %%
def fun_with_complex_args(pos1, pos2, /, pos_or_key, *, key1, key2):
    """复合参数的函数，
    /之前的参数只能用位置参数的方式调用，
    *之后的参数只能用关键字参数的方式调用，
    中间的参数两种方式都可以"""
    pass


fun_with_complex_args(1, 2, 3, key1="", key2=2)
fun_with_complex_args(1, 2, pos_or_key=3, key1=1, key2=2)


# %%

import time  # noqa: E402


def measure(func):
    def wrapper(*args, **kargs):
        t1 = time.time()
        result = func(*args, **kargs)
        t2 = time.time()
        print(f"{func.__name__} finished in {t2-t1} seconds")
        return result

    return wrapper


@measure
def do_something():
    time.sleep(1.5)


@measure
def do_something_hard():
    time.sleep(2.5)


do_something()
do_something_hard()

# %%
