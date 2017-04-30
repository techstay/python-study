# Q1
guess_me = 7

if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

# Q2
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1

# Q3
for i in [3, 2, 1, 0]:
    print(i)

# Q4
even = [i for i in range(1, 10) if i % 2 == 0]

# Q5
squares = {k: k ** 2 for k in range(1, 10)}

# Q6
odd = {i for i in range(1, 10) if i % 2 != 0}

# Q7
for thing in (f'Got {i}' for i in range(1, 10)):
    print(thing)


# Q8
def good():
    return ['Harry', 'Ron', 'Hermione']


# Q9
def get_odds():
    for i in range(1, 10, 2):
        yield i


for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print(f'Third odd is {number}')


# Q10
def test(func):
    def new_func(*args, **kargs):
        print('start')
        result = func(*args, **kargs)
        print('end')
        return result

    return new_func


@test
def hello():
    print('Hello !')


hello()


# Q11
class OopsException(Exception):
    pass


try:
    raise OopsException()
except OopsException as ex:
    print('Caught an oops')

# Q12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movies = dict(zip(titles, plots))
print(movies)
