print('Hello Python')

7 * 13
7 / 3

7  # int
2.7  # float

# floating points are not accurate
0.1 + 0.2
round(0.1 + 0.2, 3)
7 // 3

# REPL: Read, Eval, Print, Loop
# AKA: Interactive Prompt

# "python file.py" does on RE

2**10  # kb
2**1000

import math

math.sqrt(2)

# kb is variable
# variables don't a type
# the type is the type of the object they point to
kb = 2**10
10 * kb

kb = 'kilobyte'
print(kb)

count = 10
if count > 5:
    print('big enough')
    print('really big')
print('out of "if"')

# C/C++/Javascript ...
# if count > 5 {
#    print('big enough')
# }

if count > 50:
    print('very big')
elif count > 20:
    print('big-ish')
else:
    print('small')

# Now "switch" in Python

if (count > 5 and count < 20) or count < 0:
    print('just right')

# Always code as if the guy who ends up maintaining your code
# will be a violent  psychopath who knows where you live.
#    - Martin Golding

# n is a variable
# range is half-open: up to but not including last
for n in range(4):
    print(n)

for n in range(1, 4):
    print(n)

for n in range(1, 40, 7):
    print(n)

# Total of numbers from 1 to 100
total = 0
for n in range(1, 101):
    total += n
    # total = total + n
print(total)

# % is the modulo operator (reminder)
8 % 4
8 % 3

# Euler 1
# https://projecteuler.net/problem=1
# Find the sum of all the multiples of 3 or 5 below 1000.
# Answer: 233168
# print(233168)

# GPAO: Get, Parse, Analyze, Output
# Get
total = 0
# for every number below 1000
for n in range(1000):
    # Parse (NOP)
    # Analyze
    # if the number is a mulitple of 3 or 5
    if n % 3 == 0 or n % 5 == 0:
        # add it to sum
        total += n
# Output
# print sum
print(total)

for n in range(10):
    if n > 5:
        break  # stop the loop (finding)
    print(n)

for n in range(10):
    if n % 2 == 0:
        continue  # move to next iteration (filtering)
    print(n)

n = 1
while n < 5:
    print(n)
    n += 1

n = 1
while True:
    if n > 5:
        break
    print(n)
    n += 1

# unpacking
hero1, hero2 = 'Clark', 'Bruce'
print(hero1, hero2)

hero1, hero2 = hero2, hero1
print(hero1, hero2)

# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.
# Answer:  4613732

# GPAO
# Write the solution in English, then translate to Python
