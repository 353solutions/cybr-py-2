from pathlib import Path

# Open a file with open
# Three ways to open a file
# - r (read), default
# - w (write), will truncate the file
# - a (append)
# There are two modes to open a file
# - t (text), default
# - b (binary)
# fp = open('data/prices.csv')  # 'rt' - the default
fp = open('data/unicode.png', 'rb')
data = fp.read()
print(type(data))  # str in 'rt' and bytes in 'rb'
fp.close()


fp = open('data/prices.csv')  # 'rt' - the default
# A "for loop" on an open file will return lines
for line in fp:
    # print(line, end='')
    # print(line.rstrip())
    print(line[:-1])


# "with" statment (context manager) is used to handle resources

with open('data/prices.csv') as fp:
    print('in:', fp.closed)
    # 1 / 0
print('out:', fp.closed)

# Exercise: print out file name and line number
# in all chapters that contain the word Sherlock
# $ grep -i -n Sherlock data/sherlock/*.txt

# Get
for file in Path('data/sherlock').glob('*.txt'):
    with open(file) as fp:
        for lnum, line in enumerate(fp, 1):
            # Parse: NOP
            # Analyze
            if 'sherlock' in line.lower():
                # Output
                print(f'{file}:{lnum} {line}', end='')
