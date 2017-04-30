# Q1
import zoo

zoo.hours()

# Q2
import zoo as menagerie

menagerie.hours()

# Q3
from zoo import hours

hours()

# Q4
from zoo import hours as info

info()

# Q5
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

# Q6
from collections import OrderedDict

fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)

# Q7
from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists['a'] = 'something for a'
print(dict_of_lists['a'])
