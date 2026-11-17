# Q7 - Day-4 Design Challenge
# Selected program: Q4 string building.
# Compare original repeated += with redesigned join() using identical data.

import time

def original_build(parts):
    text = ""
    for part in parts:
        text += part + ";"
    return text

def redesigned_build(parts):
    return ";".join(parts) + ";"

def run_test(function, parts, repeats=3):
    times = []
    output = ""
    for _ in range(repeats):
        start = time.perf_counter()
        output = function(parts)
        times.append(time.perf_counter() - start)
    return output, times, sum(times) / len(times)

if __name__ == "__main__":
    print("Q7: Original vs redesigned string builder")
    for size in (1_000, 10_000, 200_000):
        data = [f"Item{i}:Rs{i % 50}" for i in range(size)]
        old_output, old_runs, old_avg = run_test(original_build, data)
        new_output, new_runs, new_avg = run_test(redesigned_build, data)

        improvement = old_avg / new_avg if new_avg > 0 else float("inf")
        print(f"\\nInput size: {size}")
        print("Outputs identical:", old_output == new_output)
        print(f"Original runs: {old_runs}")
        print(f"Redesigned runs: {new_runs}")
        print(f"Original average: {old_avg:.6f} s")
        print(f"Redesigned average: {new_avg:.6f} s")
        print(f"Speed-up ratio (original / redesigned): {improvement:.2f}x")

# Diagnosis: repeated += may repeatedly allocate/copy growing strings.
# Objective: reduce average time while producing exactly the same output.
# Redesign: collect pieces and join them once.
# Trade-off: join requires the input pieces and final output in memory.
# Expected: join scales more predictably for large inputs. Actual results
# depend on Python implementation, machine and memory; report measured data.
