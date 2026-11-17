import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    M = int(input_data[1])

    # Dictionary to track the degree of each node
    degrees = {}

    # Initialize all nodes with 0 degree so isolated nodes are accounted for
    for i in range(N):
        degrees[i] = 0

    # Variables to track the node with the highest degree and its max degree
    best_node = 0
    max_degree = 0

    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2

        # Increment degrees in the dictionary
        degrees[u] += 1
        degrees[v] += 1

        # Check and update the best node if u or v now has the highest degree
        if degrees[u] > max_degree:
            max_degree = degrees[u]
            best_node = u

        if degrees[v] > max_degree:
            max_degree = degrees[v]
            best_node = v

    # Total observed agents = neighbors + the hacked node itself
    # (If N == 0, X would be 0)
    X = max_degree + 1 if N > 0 else 0

    # Formula: X * (X - 1) // 2
    total_pairs = (X * (X - 1)) // 2

    print(total_pairs)


if __name__ == "__main__":
    solve()