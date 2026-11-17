# Task06 – Recursion and Its Limits

### Problem Statement
Develop a Python program to calculate the number of ways to climb temple steps by taking either one or two steps at a time.

### Concepts Used
- Recursion
- Base case
- Recursive case
- Memoisation
- functools.lru_cache
- Function call counting
- Iteration
- Recursion limit

### Files Included
- Task06_Recursion_Memoisation_and_Loop.py
- Output screenshots
- Function call measurements

### Execution Command
```bash
python Task06_Recursion_Memoisation_and_Loop.py
```

### Implementation
The program compares plain recursion, memoised recursion and an iterative approach to calculate stair-climbing combinations.

### Testing
Tested different staircase sizes and compared function calls for n = 10, 20, 25 and 30. Also examined the recursion limit for n = 1000.

### Result
Successfully implemented and compared recursive, memoised and iterative solutions.

### Complexity Analysis
- Plain recursion: O(φⁿ) time and O(n) stack space.
- Memoisation: O(n) time and O(n) space.
- Iteration: O(n) time and O(1) auxiliary space.
