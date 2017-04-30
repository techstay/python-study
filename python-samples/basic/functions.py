print('--------------简单函数--------------')


def im_a_function():
    print("I'm a function")


im_a_function()

print('--------------带参数的函数--------------')


def function_with_param(n=1):
    print(f'n={n}')


function_with_param(10)

print('--------------关键字参数--------------')


def function_with_keywords_arguments(a, b, c, d):
    print(f'a={a},b={b},c={c},d={d}')


function_with_keywords_arguments(b=1, a=2, d=4, c=3)

print('--------------任意参数列表--------------')


def function_with_varargs(*args):
    for arg in args:
        print(arg, end=',')
    print()


function_with_varargs(1, 2, 34, 'fuck')

print('--------------解包参数列表--------------')


def function_with_unpacking_args(**argMap):
    for k, v in argMap.items():
        print(f'[{k}:{v}]', end=' ')
    print()


function_with_unpacking_args(name='yitian', age=24, gender='male')

args = {'a': 5, 'b': 6, 'c': 1, 'd': 2}
function_with_keywords_arguments(**args)

print('--------------函数注解--------------')


def printFunctionAnnotation(a: str, b: int, c: list) -> None:
    print(printFunctionAnnotation.__annotations__)
    pass


printFunctionAnnotation('str', 22, [])

print('--------------lambda函数--------------')

im_a_lambda = lambda a, b: a + b

print(f'a+b={im_a_lambda(3,4)}')

print('--------------文档字符串--------------')


def function_with_documents():
    '''\
这是一个文档字符串
    '''
    pass


print(f'文档:{function_with_documents.__doc__}')

print('--------------装饰器--------------')


def surround_decorator(func):
    def new_func(*args, **kargs):
        print('func_start')
        result = func(*args, **kargs)
        print('func_end')
        return result

    return new_func


@surround_decorator
def hello():
    print('Hello !')


hello()
