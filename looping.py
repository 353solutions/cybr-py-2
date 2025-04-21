loons = ['bugs', 'daffy', 'tweety']
colors = ['gray', 'black', 'yellow']

# loons.reverse()  # in place, will change loons

# Print names in reverse order
for name in reversed(loons):  # won't change loons
    print(name)

for name in loons[::-1]:
    print(name)

# Print name and position
for i, name in enumerate(loons):
    print(f'{name} at {i}')

# for e in enumerate(loons):
#     # Unpacking
#     i, name = e
#     print(f'{name} at {i}')

# Print name and color
for i, name in enumerate(loons):
    color = colors[i]
    print(f'{name} is {color}')

for name, color in zip(loons, colors):
    print(f'{name} is {color}')


# zip stops at the shortest sequence
for name, color in zip(loons, colors + ['green']):
    print(f'{name} is {color}')

for name, color in zip(loons, colors + ['green'], strict=True):
    print(f'{name} is {color}')


from itertools import zip_longest

for name, color in zip_longest(loons, colors + ['green']):
    print(f'{name} is {color}')