# Defining & calling functions

def sub(a, b):
    return a - b

# positional arguments
print(sub(1, 7))

# keyword arguments
print(sub(a=1, b=7))
print(sub(b=7, a=1))

# a positional, b keyword
print(sub(1, b=7))

# error, positional must come before keyword
# print(sub(a=1, 7))

args = (1, 7)
# print(sub(args[0], args[1]))
# * in a function call will unpack sequence to positional
print(sub(*args))

print(1)
print(1, 2)

# * in function definition will convert positional to a tuple
def var_args(*args):
    # args is a tuple
    print(f'{args=}')

var_args()
var_args(1)
var_args(1, 2)

args = {'a': 1, 'b': 7}
# ** in function call convert mapping to keyword
print(sub(**args))
# print(sub(a=1, b=7))

# ** in function definition will convert keyword to a dict
def kw_args(**kw):
    # kw is a dict
    print(f'{kw=}')

kw_args()
kw_args(a=1)
kw_args(a=1, b=7)

# **kw use case: pass through options
def plot(xs, ys, color='black', width=1, marker='o', alpha=1):
    print(f'plot: {xs=}, {ys=}')


from datetime import datetime

def load_from_db(date: datetime):
    pass


def plot_monthly_report(date, **kw):
    data = load_from_db(date)
    xs, ys = data['day'], data['revenue']
    plot(xs, ys, **kw)


# if the user does not supply b, use 1
# WARNING: Never use mutable default value
# e.g. def add_to(value, items=[]):
def add(a, b=1):
    return a + b

print(add(2, 7))
print(add(7))


# type hints
def mul(a: int, b: int) -> int:
    return a * b

print(mul(7, 8))
print(mul('x', 10))

# Miki's usage for type hints:
# - Documentation
# - Help the . (autocompletion)

def append_one(n: list):
    n.append(1)


div_call_count = 0
div_times = []

# mutation vs re-binding
# You can re-bind only in the same scope

def div(a, b):
    global div_call_count

    div_times.append(datetime.now())  # mutation
    div_call_count += 1  # re-bind
    # div_call_count = div_call_count + 1
    return a / b


print(div(1, 7))
print(div_call_count)
print(div_times)

# Use global only if you re-bind
# If you mutate or just read the value - you don't need to


y = 10
def fn():
    # x is local to fn
    # it is not accessible outside of it
    # x scope is the function
    x = 1

fn()
# print(x)  # error: x is not accessible outside fn

# Python has 4 scopes: LCGB
# local: function (x)
# closure/enclosing
# global (y)
# bulit-in