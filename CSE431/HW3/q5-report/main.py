import timeit
import random
import matplotlib
matplotlib.use('TkAgg')  # Uses standard OS window instead of PyCharm's backend
import matplotlib.pyplot as plt

# https://www.programiz.com/dsa/insertion-sort
def insertion(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key
    return array

k = 90  # threshold where insertion sort takes over small sub-arrays
# https://www.w3schools.com/python/python_dsa_mergesort.asp
def merge_sort(list, use_hybrid = False):

    def sort(arr):
      if len(arr) <= 1:
        return arr

      mid = len(arr) // 2
      leftHalf = arr[:mid]
      rightHalf = arr[mid:]

      sortedLeft = sort(leftHalf)
      sortedRight = sort(rightHalf)

      return merge(sortedLeft, sortedRight)

    def merge(left, right):
      result = []
      i = j = 0

      while i < len(left) and j < len(right):
        if left[i] < right[j]:
          result.append(left[i])
          i += 1
        else:
          result.append(right[j])
          j += 1

      result.extend(left[i:])
      result.extend(right[j:])

      return result

    def hybrid_sort(arr):
        if len(arr) <= k:
            return insertion(arr)
        mid = len(arr) // 2
        return merge(hybrid_sort(arr[:mid]), hybrid_sort(arr[mid:]))

    if use_hybrid:
        return hybrid_sort(list)
    else:
        return sort(list)



k = 90 # constant for hybrid crossover list length
if __name__ == "__main__":
    input_max = 200
    trials = 500 # for timeit
    n_values = []
    insertion_times = []
    merge_times = []
    hybrid_times = []
    for data_len in range(2, input_max):
        # Fresh unsorted data for this input size
        test_data = [random.randint(0, 100000) for _ in range(data_len)]
        t_ins = timeit.timeit(lambda: insertion(test_data.copy()), number=trials) / trials
        t_mrg = timeit.timeit(lambda: merge_sort(test_data.copy()), number=trials) / trials
        t_hyb = timeit.timeit(lambda: merge_sort(test_data.copy(), use_hybrid=True), number=trials) / trials
        n_values.append(data_len)
        insertion_times.append(t_ins)
        merge_times.append(t_mrg)
        hybrid_times.append(t_hyb)

    # plotting
    plt.plot(n_values, insertion_times, label="Insertion Sort")
    plt.plot(n_values, merge_times, label="Merge Sort")
    plt.plot(n_values, hybrid_times, label="Hybrid Sort")
    plt.xlabel("n (input size)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig("sorting_comparison.png")
    plt.show()
