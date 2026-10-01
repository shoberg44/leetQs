import bisect

numbers = []

num_tests = int(input())
for _ in range(num_tests):
    op, value = input().split()
    value = int(value)

    if op == "a":
        # inserts the value while maintaining order
        bisect.insort(numbers, value)
    elif op == "r":
        # divides the array into two parts
        divide_index = bisect.bisect_left(numbers, value)
        if divide_index < len(numbers) and numbers[divide_index] == value:
            numbers.pop(divide_index)
        else:
            print("Wrong!")
            continue

    n = len(numbers)
    # ensure last op didnt empty the list
    if n == 0:
        print("Wrong!")
    elif n % 2 == 1:
        print(numbers[n // 2])
    else:
        split = numbers[(n - 1) // 2] + numbers[n // 2]
        print(split // 2 if split % 2 == 0 else split / 2)