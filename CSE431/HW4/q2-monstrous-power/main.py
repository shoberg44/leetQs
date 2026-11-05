N = int(input())
monsters = [int(x) for x in input().split()]

# initialize to low monster count, these get override
prev2 = 0
prev1 = 0

for monster in monsters:
    current = max(prev1, prev2 + monster)
    prev2 = prev1
    prev1 = current

print(prev1)