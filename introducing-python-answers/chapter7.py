# Q1
mystery = '\U0001f4a9'

import unicodedata

print(unicodedata.name(mystery))

# Q2
pop_bytes = mystery.encode('utf8')
print(pop_bytes)

# Q3
pop_string = pop_bytes.decode('utf8')
print(pop_string)
print(mystery == pop_string)

# Q4
poem = '''My kitty cat likes %s
My kitty cat likes %s
My kitty cat fell down his %s
And now he's a %s
'''
args = ('roast beef', 'ham', 'head', 'clam')
print(poem % args)

# Q5
# 太长了，我就不写了
letter = '''Hello, {name}'''

# Q6
response = {'name': 'yitian'}
print(letter.format(**response))

# Q7
mammoth = '''\
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.'''

# Q8
import re

results = re.findall(r'\bc\w*', mammoth)
print(results)

# Q9
results = re.findall(r'\bc\w{3}\b', mammoth)
print(results)

# Q10
results = re.findall(r'\b\w*r\b', mammoth)
print(results)

# Q11
results = re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', mammoth)
print(results)

# Q12
import binascii

hex_str = '47494638396101000100800000000000ffffff21f9' + \
          '0401000000002c000000000100010000020144003b'

gif = binascii.unhexlify(hex_str)

# Q13
is_valid_gif = gif[:6] == b'GIF89a'
print(is_valid_gif)

# Q14
import struct

width, height = struct.unpack('<HH', gif[6:10])

print((width, height))
