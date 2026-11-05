ret = []
num_tests = int(input())
for _ in range(num_tests):
  _, monsters = [int(x) for x in input().split()]
  logic_gates = sorted([int(x) for x in input().split()])

  # allocate the space. each index represents a monsters splitting technique count
  previous_solutions = [0] * (monsters + 1)
  # there is one way to make a 0 monster gate
  previous_solutions[0] = 1

  for monster_combination in range(1, monsters + 1):
      # count up each prev gate when finding previous solutions
      for gate in logic_gates:
          if gate > monster_combination:
              break
          previous_solutions[monster_combination] += previous_solutions[monster_combination - gate]
      previous_solutions[monster_combination] %= 1000000009
  ret.append(previous_solutions[-1])

for value in ret:
    print(value)