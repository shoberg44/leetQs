num_tests = int(input())
start_index = 0
health = 0
for tower_n in range(num_tests):
    gained, lost = input().split()
    net = int(gained) - int(lost)
    health += net
    # route not viable, flag current run as invalid
    if health < 0:
        start_index = -1
        health = 0
    # if valid placement and no previous run
    elif start_index == -1 and health >= 0:
        start_index = tower_n
print(start_index)