import sys

# needed for some test cases
sys.setrecursionlimit(3000)

#  determines if a total can be formed from known combinations
def can_form(total):
  if total in known_formations:
    return known_formations[total]

  for monsters in gate_monster_requirements:
    if monsters > total:
      break
    if can_form(total - monsters):
      known_formations[total] = True
      return True
  known_formations[total] = False
  return False

# iterate through each test
num_tests = int(input())
for _ in range(num_tests):
  num_gates, limit = [int(x) for x in input().split()]
  gate_monster_requirements = sorted([int(x) for x in input().split()])
  # memoization dictionary
  known_formations = {0: True}
  # from limit and down for the highest valid total
  current_max = 0
  for target in range(limit, -1, -1):
    if can_form(target):
      current_max = target
      break

  print(current_max)