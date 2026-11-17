def solve():
    first_line = input().split()
    number_of_connections = int(first_line[0])
    number_of_edges = int(first_line[1])

    # degree of each node
    degrees = {}

    for i in range(number_of_connections):
        degrees[i] = 0

    max_degree = 0
    for row in range(number_of_edges):
        # get current row
        u, v = input().split()
        u = int(u)
        v = int(v)
        # update degrees in the dictionary
        degrees[u] += 1
        degrees[v] += 1
        max_degree = max(max_degree, degrees[u], degrees[v])

    max_degree = max_degree + 1 if number_of_connections > 0 else 0
    total_pairs = (max_degree * (max_degree - 1)) // 2
    print(total_pairs)


if __name__ == "__main__":
    solve()