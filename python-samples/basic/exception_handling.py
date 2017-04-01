print('--------------处理异常--------------')


class MyError(Exception):
    pass


try:
    raise MyError()
except (NameError, ValueError) as ex:
    print(f'This is a NameError:{ex}')
except MyError:
    print('This is MyError')
    raise
else:
    print('Else clause')
finally:
    print('This is finally clause')


