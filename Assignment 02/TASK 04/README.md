# Task04 – Building Long Text: + or join()?

### Problem Statement
Develop and compare different methods of building large text statements for a monthly SMS billing system.

### Concepts Used
- String concatenation
- += operator
- join() method
- f-strings
- String immutability
- time.perf_counter()

### Files Included
- Task04_Building_Long_Text_and_Timing.py
- Output screenshots
- Timing results

### Execution Command
```bash
python Task04_Building_Long_Text_and_Timing.py
```

### Implementation
The program builds text using repeated +=, join() and f-strings and measures their execution times.

### Testing
Tested with 1,000, 10,000 and 200,000 lines. Each method was executed three times to calculate average execution time.

### Result
Successfully compared different string-building techniques and analysed their performance.

### Complexity Analysis
join() takes O(n) time in the total output size. Repeated concatenation may require up to O(n²) character copying in the general case.
