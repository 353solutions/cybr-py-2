# Data types: list, tuple, dict
# Already talked: numbers (int, float), text (str, bytes)

## list
cart = ['apple', 'lemon']
print('len:', len(cart))
print('cart[0]:', cart[0])
cart.append('milk')
print('cart:', cart)
last = cart.pop()
print('last:', last)
print('cart:', cart)
cart += ['milk', 'honey']
print('cart:', cart)
print(cart.reverse())  # mutation
# When a method returns None, it means it changed the object
print('cart:', cart)

print('cart[1:]:', cart[1:])
print('cart[1:3]:', cart[1:3])
print('cart[:3]:', cart[:3])

empty_list = []  # = list()

## tuple
# Immutable ordered sequence of items
player1 = ('Parzival', 139)
print(player1)
print('len:', len(player1))
# player1[0] = 'Art3mis' # raise an error
# can be key in a dict

empty_tuple = ()

list_one = [1]
# tuple_one = (1)  # BUG: This is the number 1
tuple_one = (1,)
# tuple_one = 1,  # This is a tuple as well, confusing :)
print('list_one:', list_one)
print('tuple_one:', tuple_one)


## dict
# AKA hash table, table
# mapping from key to a value

# env -> host, port
hosts = {
    'prod': ('srv1', 80),
    'qa': ('srv2', 8080),
}
print(hosts['qa'])
print(hosts['qa'][1])  # qa port

heros = {
    'Clark': 'Superman',
    'Diana': 'Wonder Woman',
    'Bruce': 'Batman',
}

# iterate over the keys
for name in heros:
    print(name)

# iterate over the values
for hero in heros.values():
    print(hero)

x, y = (1, 2)  # unpacking

for name, hero in heros.items():
    print(f'{name} is {hero}')

heros['Steve'] = 'Captain America'
print(heros)
# del heros['Steve']
h = heros.pop('Steve')
print('h:', h)
print(heros)

# print(heros['Joe'])  # will raise on missing key
print(heros.get('Joe'))  # Returns None on missing key
print(heros.get('Diana'))

print('Joe' in heros)
print('Joe' not in heros)


# Aside
# str is immutable, list is mutable
s = 'hello'
print(s.upper())
print('s:', s)
s = s.upper()  # re-binding
print('s:', s)

# equality vs identity
l1, l2 = ['rick', 'morty'], ['rick', 'morty']
print(l1 == l2)  # equality
print(l1 is l2)  # identity
l1.append('beth')
print('l1:', l1)
print('l2:', l2)


poem = '''
The Road goes ever on and on
Down from the door where it began
Now far ahead the Road has gone
And I must follow if I can
Pursuing it with eager feet
Until it joins some larger way
Where many paths and errands meet
And whither then I cannot say
'''
# Bilbo Baggins (LOTR)

# Exercise: What is the most common word
# in the poem? Extra: ignore case

# word -> count
freq = {}

# Get
words = poem.split()
for word in words:
    word = word.lower()
    # freq[word] += 1  # will err
    freq[word] = freq.get(word, 0) + 1

max_word, max_count = '', 0
# Analyze
for word, count in freq.items():
    if count > max_count:
        max_word, max_count = word, count

# Output
print(max_word)
