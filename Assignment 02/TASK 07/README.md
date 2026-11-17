# Task07 – Diagnose, Redesign and Validate

### Problem Statement
Analyse an existing program, identify its performance limitations and develop an improved solution with experimental validation.

### Selected Program
Task04 – Building Long Text

### Concepts Used
- Performance analysis
- Bottleneck identification
- Program redesign
- String concatenation
- join() method
- time.perf_counter()
- Experimental comparison
- Time and space complexity

### Files Included
- Task07_Diagnose_Redesign_Validate.py
- Output screenshots
- Performance comparison results

### Execution Command
```bash
python Task07_Diagnose_Redesign_Validate.py
```

### Implementation
The original string-building approach using repeated += is compared with the redesigned approach using join().

### Testing
Both implementations are tested with identical inputs containing 1,000, 10,000 and 200,000 items. Each is executed three times to calculate average execution time.

### Result
Successfully diagnosed a performance limitation, redesigned the program and compared both implementations using execution time and output correctness.

### Complexity Analysis
The original approach may require up to O(n²) character copying in the general case, while the redesigned join() approach takes O(n) time in the total output size.

### Conclusion
The redesigned solution provides a more suitable approach for building large strings while preserving the original output.
