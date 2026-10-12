# Empirical Evaluation of Sorting Algorithms: Insertion Sort vs. Merge Sort
**Name:** [Your Name]  
**Course:** CSE 431  

---

## 1. Hypothesis
* **Initial expectation:** State what range of $n$ you expect Insertion Sort to win, and where you expect the lines to cross (e.g., *"I hypothesize that Insertion Sort will be faster than Merge Sort for $n < 30$ due to lower constant-factor overhead, function call elimination, and in-place swapping..."*).
* **Rationale:** Mention why Merge Sort's theoretical $O(n \log n)$ is hindered at small $n$ (recursive calls, list slicing/allocations, and merge copies).

---

## 2. Methods
* **System Environment:** 
  - Language & Version: Python 3.12 (or whichever version you run)
  - Hardware: OS (e.g., Windows 11), CPU model, RAM.
* **Algorithm Implementation:**
  - Standard in-place Insertion Sort.
  - Recursive Merge Sort.
  - Link to repository/code or include code snippets in appendix.
* **Testing Protocol:**
  - Tested $n$ from $2$ to $250$.
  - Used `random.randint` with a consistent seed/generation pattern.
  - To prevent testing on already-sorted lists, made separate `.copy()` arrays for each trial.
  - Used `time.perf_counter()` over $1,000$ trials per $n$ to minimize OS background noise and clock quantization errors.

---

## 3. Results
* **Plot:** Embed `sorting_comparison.png` here. Make sure axes (Input size $n$, Time in $\mu s$) and legend are clearly visible.
* **Observation:**
  - State the exact $n$ or range where the two curves intersect.
  - Describe the trajectory: Insertion sort starts lower, curves quadratically upward ($O(n^2)$), while Merge sort grows much more gently ($O(n \log n)$).

---

## 4. Discussion
* **Analysis of Crossover:**
  - Was the crossover point earlier or later than your hypothesis?
  - Why does Insertion Sort win for small $n$? (Cache locality, no recursion overhead, minimal memory allocations).
  - Python-specific effects (e.g., list slicing `arr[:mid]` creating new copies in Python can inflate Merge Sort's constant factor).
* **Experimental Challenges:**
  - Did CPU frequency scaling, garbage collection, or OS background tasks create spikes? How did averaging over 1,000 runs address that?

---

## 5. Conclusions
* State a concise, concrete takeaway:
  - *"Under the tested environment, Insertion Sort is faster for $n < X$, while Merge Sort is consistently superior for $n > Y$. Between $n = X$ and $n = Y$, the performance is indistinguishable."*
  - Mention practical implications (e.g., why hybrid algorithms like Timsort switch to binary insertion sort for small run lengths).