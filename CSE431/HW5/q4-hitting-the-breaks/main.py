first_line = input().split()
number_of_nodes = int(first_line[0])
number_of_edges = int(first_line[1])

# I will be using my own implementation of Kruskal's algorithm

# gather edges
edges = []
for _ in range(number_of_edges):
    u, v, cost = input().split()
    u = int(u)
    v = int(v)
    cost = int(cost)
    edges.append((cost, u, v))
# sort to use cheapest edges first
edges.sort()

# tracks the owner of a component. start with each node as a distinct island
owner_tracker = [i for i in range(number_of_nodes)]
# find the owner of a component
def find_owner(n):
    if owner_tracker[n] != n: # owners point to themselves
        owner_tracker[n] = find_owner(owner_tracker[n])
    return owner_tracker[n]

def merge_components(u, v):
    u_owner = find_owner(u)
    v_owner = find_owner(v)

    # if two islands, merge their root owners
    if u_owner != v_owner:
        owner_tracker[v_owner] = u_owner
        return True
    # dont remerge sets with the same owner, this creates a counter productive loop
    return False

ret_cost = 0
edges_used = 0
for cost, u, v in edges:
    if merge_components(u, v):
        ret_cost += cost
        edges_used += 1
        # we should need 1 edge for 2 nodes, and 2 edges for 3 and so on...
        if edges_used == number_of_nodes - 1:
            break
print(ret_cost)
