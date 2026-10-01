max_stack = []

num_tests = int(input())
for test_idx in range(num_tests):
    line = input().split()
    operation = int(line[0])
    if operation == 1:
        val = int(line[1])
        cur_max = None
        # find largest
        if not max_stack:
            cur_max = val
        elif val > max_stack[-1]:
            cur_max = val
        else:
            cur_max = max_stack[-1]
        max_stack.append(cur_max)
    elif operation == 2:
        if max_stack:
            max_stack.pop()
    elif operation == 3:
        if max_stack:
            print(max_stack[-1])