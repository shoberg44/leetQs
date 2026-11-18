first_line = input().split()
number_of_nodes = int(first_line[0])
number_of_edges = int(first_line[1])
# every node has a set of connected nodes
neighbors = {}
for i in range(number_of_nodes):
    neighbors[i] = set()

# Store all edges so we can test each adjacent pair
edges = []

for row in range(number_of_edges):
    u, v = input().split()
    u = int(u)
    v = int(v)
    # add this neighbor to the respective nodes tracked neighbors
    neighbors[u].add(v)
    neighbors[v].add(u)
    edges.append((u, v))

# look for max(degree) or two combined nodes
max_agents = 0
# the correct pair are required to be connected, thus we iterate through the conenctions
for u, v in edges:
    # union this pair to see if the node combination is the largest
    max_agents = max(len(neighbors[u] | neighbors[v]), max_agents)

total_pairs = (max_agents * (max_agents - 1)) // 2
print(total_pairs)