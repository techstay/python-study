# Q1
year_list = [1994, 1995, 1996, 1997, 1998]

# Q2
third_year = year_list[3]

# Q3
max_year = max(year_list)

# Q4
things = ['mozzarella', 'cinderella', 'salmonella']

# Q5
things[1].capitalize()
print(things)

# Q6
things[0].upper()
print(things)

# Q7
del things[-1]
print(things)

# Q8
surprise = ['Groucho', 'Chico', 'Harpo']
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()

# Q10
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'norse'}
print(e2f)

# Q11
print(e2f['walrus'])

# Q12
f2e = {}
for k, v in e2f.items():
    f2e.setdefault(v, k)

print(f2e)

# Q13
print(f2e['chien'])

# Q14
set(e2f.keys())

# Q15
life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'others': {}
}

# Q16
print(life.keys())

# Q17
print(life['animals'].keys())

# Q18
print(life['animals']['cats'])
