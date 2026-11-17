# Q6 - Recursion and Its Limits
from functools import lru_cache
import sys
import time

calls_naive = 0
calls_memo = 0

def ways_naive(n):
    """Plain recursive solution."""
    global calls_naive
    calls_naive += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@lru_cache(maxsize=None)
def ways_memo(n):
    """Memoised recursive solution."""
    global calls_memo
    calls_memo += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def ways_loop(n):
    """Iterative solution storing only the previous two values."""
    if n <= 1:
        return 1
    previous, current = 1, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current

def measure_calls(n):
    global calls_naive, calls_memo
    calls_naive = 0
    naive_answer = ways_naive(n)
    naive_count = calls_naive

    ways_memo.cache_clear()
    calls_memo = 0
    memo_answer = ways_memo(n)
    memo_count = calls_memo
    return naive_answer, naive_count, memo_answer, memo_count

if __name__ == "__main__":
    print("Answers by hand-check range:")
    for n in range(1, 7):
        print(f"n={n}: {ways_loop(n)}")

    print("\\nFunction-call comparison:")
    for n in (10, 20, 25, 30):
        answer, naive_count, memo_answer, memo_count = measure_calls(n)
        print(f"n={n}: answer={answer}, naive calls={naive_count}, "
              f"memo calls={memo_count}")

    print("\\nRecursion limit:", sys.getrecursionlimit())
    ways_memo.cache_clear()
    try:
        print("Memoised result for 1000:", ways_memo(1000))
    except RecursionError:
        print("RecursionError: recursion depth exceeded; memoisation does "
              "not remove the recursive call stack.")

    start = time.perf_counter()
    result = ways_loop(1000)
    elapsed = time.perf_counter() - start
    print("Loop result for 1000:", result)
    print(f"Loop time: {elapsed:.6f} seconds")

# Plain recursion: O(phi^n) time and O(n) stack.
# Memoisation: O(n) time, O(n) cache and O(n) stack.
# Iteration: O(n) time and O(1) auxiliary space.
# For n=1000, iteration is the safest deployment choice.
