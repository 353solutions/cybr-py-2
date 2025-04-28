from pprint import pprint

# sum of squares up to 10

## option 1
total = 0
for i in range(10):
    total += i*i
print(total)

## option 2
squares = []
for i in range(10):
    squares.append(i*i)
print(sum(squares))

## option 3
# List comprehension: A way to create a new list
# If you see code like option 2, use list comprehension
squares = [i*i for i in range(10)]
print(sum(squares))

## option 4: compress option 3
print(sum([i*i for i in range(10)]))

# sum of squares up to 10, only odd numbers

print(sum([i*i for i in range(10) if i % 2 == 1]))

# syntax: [operation for ... in ... (if ...)]
# SQL: [SELECT ... FROM ... WHERE ...]

loons = ['Bugs', 'Daffy', 'Taz']
# change (map)
print([name.upper() for name in loons])

# filter
print([name for name in loons if len(name) > 3])

# map + filer
print([name.upper() for name in loons if len(name) > 3])


stocks_data = '''\
CSCO,100,18.04
TSLA,200,45.03
CSCO,150,19.05
MSFT,250,80.56
IBM,500,22.01
TSLA,250,44.23
GOOG,200,501.45
CSCO,175,19.56
MSFT,75,80.81
GOOG,300,502.65
IBM,150,25.01
'''

# convert data to a list of dicts
# [
#   {'symbol': 'CSCO', 'volume': 100, 'price': 18.04},
# ]
# IRL use the csv module
# In CSV, everything is parsed to a str

def parse_line(line):
    '''
    >>> parse_line('CSCO,100,18.04')
    {'symbol': 'CSCO', 'volume': 100, 'price': 18.04}
    '''
    symbol, volume, price = line.split(',')
    return {
        'symbol': symbol,
        'volume': int(volume),
        'price': float(price),
    }


trades = [parse_line(line) for line in stocks_data.splitlines()]
pprint(trades)

# Print unique list of symbols
# In Python unique means set
print('We are invested in:')
symbols = [trade['symbol'] for trade in trades]
for symbol in sorted(set(symbols)):
    print(f'- {symbol}')

# How many stocks of CSCO do we own?
num_csco = sum([
    trade['volume'] 
    for trade in trades 
    if trade['symbol'] == 'CSCO'
])
print(f'We own {num_csco} stocks of CSCO')

# How much money have we invested?

invested = sum([
    trade['volume'] * trade['price']
    for trade in trades
    # no filter
])
print(f'We invested ${invested:,}')

current_data = '''\
CSCO,61.71
GOOG,156.23
IBM,248.66
MSFT,375.39
TSLA,259.16
'''