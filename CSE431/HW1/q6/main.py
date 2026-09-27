import math
ret = []

def count_multiples(low, high, n):
    """
    count integers in [low, high] divisible by n.
    floor(high / n) - floor((low - 1) / n)
    Source: https://www.geeksforgeeks.org/count-numbers-divisible-m-given-range/
    """
    return (high // n) - ((low - 1) // n)


def get_passwords(low, high):
    mults = count_multiples(low, high, 12)
    # perfect squares
    # x = n^2 lies in [low, high] if n lies in [min_n, max_n].
    # https://docs.python.org/3/library/math.html#math.isqrt
    if low > 0:
        min_n = math.isqrt(low - 1) + 1
    else:
        min_n = 0
    max_n = math.isqrt(high)

    squares = max_n - min_n + 1
    # For n^2 to be divisible by 12 (2^2 * 3), its root n must be a multiple of 6
    both = count_multiples(min_n, max_n, 6)

    ret.append([mults, squares, both])

# given template
num_tests = int(input())
for test_idx in range(num_tests):
    line = input().split()
    num_1 = int(line[0])
    num_2 = int(line[1])
    get_passwords(num_1, num_2)

for line in ret:
    # formats list to space delimited output
    print(str(line).replace(',','').strip(']').strip('['))