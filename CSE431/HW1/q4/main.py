ret = []


def find_amount(rubie_value, saph_value, backpack_space):
    if rubie_value == saph_value:
        ret.append(str(rubie_value * backpack_space))
        return
    low, high = min(rubie_value, saph_value), max(rubie_value, saph_value)
    step_diff = high - low
    # min value starting point
    base = low * backpack_space
    combinations = []
    for slot in range(backpack_space + 1):
        combinations.append(str(base + slot * step_diff))
    ret.append(" ".join(combinations))


# given template
num_tests = int(input())
for test_idx in range(num_tests):
    line = input().split()
    rubie_value = int(line[0])
    saph_value = int(line[1])
    space = int(line[2])
    find_amount(rubie_value, saph_value, space)

for line in ret:
    print(line)