stores = {}
current_max_store = None
num_tests = int(input())
for test_idx in range(num_tests):
    line = input()
    stores.setdefault(line, 0)
    mention_new_value = stores[line] + 1
    mention = line
    stores[line] = mention_new_value

    if current_max_store is None:
        current_max_store = mention
    elif stores[current_max_store] < mention_new_value:
        current_max_store = mention
    elif stores[current_max_store] == mention_new_value and int(current_max_store) > int(mention):
        current_max_store = mention

print(current_max_store)



