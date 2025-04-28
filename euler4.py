# https://projecteuler.net/problem=4


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


max_pali = 0
# Get
for i in range (100, 1000):
    for j in range(100, 1000):
        # Parse: NOP
        # Analyze
        prod = i * j
        if is_palindrome(prod) and prod > max_pali:
            max_pali = prod
# Output
print(max_pali)