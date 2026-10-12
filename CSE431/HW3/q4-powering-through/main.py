tests = int(input())

for component in range(tests):
    starting, target = input().split()
    starting, target = int(starting), int(target)
    print(int.bit_count(starting-target))
