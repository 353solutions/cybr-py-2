# All the below 4 are the same
s = 'hi' 
s = "hi" 
s = '''hi'''
s = """hi"""

# The \ remove initial newline
message = '''\
fix(python): Do rouding the right way.

Round results so they'll match documentation.
Fixes: ENG-101
'''
print(message)

# \t is TAB
# \n is newline
# \202 is 
csv_file = "c:\taxes\new\2025.csv"
print(csv_file)

# r'text' means "raw" string
# A \ is just a \
csv_file = r"c:\taxes\new\2025.csv"
print(csv_file)

what, cost = 'banana', 10.2
# f-string: formatted string
print(f'A {what} costs ${cost}. ${cost}!')

# :>10: Indent to the right, minimal size of 10
# :.2f mean floating point, two digits after the decimal
print(f'A {what:>10} costs ${cost:.2f}. ${cost:.2f}!')

n = 1234567
print(f'n = {n:,}')

for n in (1, 12, 123):
    print(f'{n:3}')

a, b = '1', 1
# !s (default): str for users
print(f'a = {a}, b = {b}')

a, b = '1', 1
# !r means "repr", for developers, adds type information
print(f'a = {a!r}, b = {b!r}')
print(f'{a=}, {b=}')

print(f'''{a}''')

template = '{count} bottles of beer on the {what}'
print(template.format(count=10, what='wall'))

book = 'The Colour of Magic'
print(book[0])
# book[0] = 't'  # error: strings are immutable
print(book[-1], book[-2])
# slicing
print(book[:3])
print(book[3:])
print(book[3:7])
print(book[3:13:4])
# print(book[3000])  # error
print(book[:3000])  # won't error
print(len(book))

# Use lower for case insensitive comparison
# In Unicode use casefold
print(book.lower())
print(book)

if book.endswith('Magic'):
    print('fantasy')

# RTFM: read the fine manual
# BUG: bool(-1) is True
if book.find('spaceship'):
    print('sci-fi')

if 'spaceship' in book:
    print('sci-fi')


# Diversion: What is True (in Python)?
print(True, False)

# In Python, everything is true. Except:
# - False
# - Zero: 0, 0.0, ...
# - Empty collections: '', [], {}, ...
# - None

shopping_cart = []
if len(shopping_cart) == 0:
    print('cart is empty')

# More Pythonic
if not shopping_cart:
    print('cart is empty')

print(book.replace('Colour', 'Color'))

loc = ' las vegas strip\n'
clean_loc = loc.strip()
print(f'|{clean_loc}|')

for c in 'I ♡ Python':
    print(c)  # c is a str

# Exercise: How many "a" (ignoring case are in "road.txt")

# Get
poem = '''
The Road goes ever on and on
Down from the door where it began.
Now far ahead the Road has gone,
And I must follow, if I can,
Pursuing it with eager feet,
Until it joins some larger way
Where many paths and errands meet.
And whither then? I cannot say.
'''
# Bilbo Baggins (LOTR)
total = 0
for c in poem:
    if c.lower() == 'a':
        total += 1
print(total)

text = 'I ♡ Python'
print(len(text))

# str -> bytes
data = text.encode()
print(len(data))

# bytes -> str
print(data.decode())

# Work with bytes only at the edges of your program
# (network, files, ...)
# send: str->bytes (encode)
# receive: bytes->str (decode)
# internally work with str

# shalom (Hebrew: Hello, Peace)
greet = 'שלום'
print(greet[0])

# You create a function with "def" keyword
# If there's no "return", the function will return None
def inc(n):
    return n + 1

# Write a function that sums numbers in a string

def sum_digits(s):
    total = 0
    for c in s:
        d = int(c)  # str -> int
        total += d
    return total

text = '123'
print(sum_digits(text))

def banner(text, width):
    ... # TODO: Your code goes here

banner('Hi', 6)
#   Hi
# ------