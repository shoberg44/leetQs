import heapq

num_tests = int(input())
instructions = []
for _ in range(num_tests):
    time, op_length = input().split()
    instructions.append((int(time), int(op_length)))
instructions.sort()

# priority queue for instructions that have arrived, ordered by shortest duration
operations_ready = []
instruction_times = []
current_time = 0
i = 0

while i < num_tests or operations_ready:
    # jump time forward to the next instruction's arrival if idle
    if not operations_ready and current_time < instructions[i][0]:
        current_time = instructions[i][0]

    # add all instructions that have arrived by current_time
    while i < num_tests and instructions[i][0] <= current_time:
        arr_time, op_len = instructions[i]
        heapq.heappush(operations_ready, (op_len, arr_time))
        i += 1

    # process the shortest available instruction
    op_len, arr_time = heapq.heappop(operations_ready)
    current_time += op_len
    instruction_times.append(current_time - arr_time)

print(sum(instruction_times) // num_tests)