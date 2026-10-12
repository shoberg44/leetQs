import time
import random
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# 1. ALGORITHM IMPLEMENTATIONS
# ---------------------------------------------------------------------------

def insertion_sort(arr):
    """In-place Insertion Sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """Standard recursive Merge Sort."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge step
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# ---------------------------------------------------------------------------
# 2. BENCHMARKING HARNESS
# ---------------------------------------------------------------------------

def benchmark():
    # Adjust range to capture where the curves cross (typically between n=10 and n=100)
    # Step by 2 or 5 for fine granularity around the crossover
    n_values = list(range(2, 100, 2)) + list(range(100, 250, 10))

    # Number of trials per n to average out OS noise
    trials = 150

    insertion_times = []
    merge_times = []

    print(f"Running benchmarks ({trials} trials per n)...")

    for n in n_values:
        # Pre-generate independent test lists to ensure identical inputs
        test_data = [[random.randint(0, 100000) for _ in range(n)] for _ in range(trials)]

        # --- Benchmark Insertion Sort ---
        # Deep copy to ensure sorting an unsorted list every time
        arrs_for_insertion = [lst.copy() for lst in test_data]

        t0 = time.perf_counter()
        for arr in arrs_for_insertion:
            insertion_sort(arr)
        t1 = time.perf_counter()
        avg_insertion_time = (t1 - t0) / trials
        insertion_times.append(avg_insertion_time)

        # --- Benchmark Merge Sort ---
        arrs_for_merge = [lst.copy() for lst in test_data]
        t0 = time.perf_counter()
        for arr in arrs_for_merge:
            merge_sort(arr)
        t1 = time.perf_counter()
        avg_merge_time = (t1 - t0) / trials
        merge_times.append(avg_merge_time)

        print(f"n = {n:3d} | Insertion: {avg_insertion_time * 1e6:6.2f} µs | Merge: {avg_merge_time * 1e6:6.2f} µs")

    # ---------------------------------------------------------------------------
    # 3. PLOTTING RESULTS
    # ---------------------------------------------------------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, [t * 1e6 for t in insertion_times], label="Insertion Sort", marker="o", markersize=3)
    plt.plot(n_values, [t * 1e6 for t in merge_times], label="Merge Sort", marker="s", markersize=3)

    plt.xlabel("Input Size (n)")
    plt.ylabel("Average Time per Sort (microseconds)")
    plt.title("Empirical Comparison: Insertion Sort vs. Merge Sort")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)

    # Save and display
    plt.savefig("sorting_comparison.png", dpi=300)
    print("Plot saved to sorting_comparison.png")
    plt.show()


if __name__ == "__main__":
    benchmark()
