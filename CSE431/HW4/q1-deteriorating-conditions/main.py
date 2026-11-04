fight_num, armor = input().split()
fight_num = int(fight_num)
armor = int(armor)

fights = [int(x) for x in input().split()]
fights.sort(reverse=True)

total_cost = 0

for i, element in enumerate(fights):
    total_cost += ((i // armor) + 1) * element

print(total_cost)