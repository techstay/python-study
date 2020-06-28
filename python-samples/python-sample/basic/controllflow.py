print('--------------if语句--------------')

i = 5
if i <= 3:
    print('1<=3 is true')
elif 4 <= i <= 5:
    print('4<=i<=5 is false')
else:
    print('others')

print('--------------while语句--------------')

it = 0
sum = 0
while it <= 10:
    sum += it
    it += 1
print(f'sum={sum}')

print('--------------for语句--------------')
for i in range(1, 10):
    print(i, end=' ')
print()

print('--------------for语句--------------')
it = 1
while it < 3:
    it += 1
else:
    print(f'else: it={it}')

print('--------------跳转语句--------------')
for i in range(1, 5):
    for j in range(1, i + 1):
        if i <= j:
            continue
        print(f'[{i},{j}]', end='')
print()
