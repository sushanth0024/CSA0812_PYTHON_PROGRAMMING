# Q4 - Building Long Text: +=, join(), and f-string line creation
import time

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    return ";".join(parts) + ";"

def build_fstring(parts):
    # Each line is created with an f-string, then joined efficiently.
    lines = [f"{p};" for p in parts]
    return "".join(lines)

def average_time(function, data, repeats=3):
    measurements = []
    result = None
    for _ in range(repeats):
        start = time.perf_counter()
        result = function(data)
        measurements.append(time.perf_counter() - start)
    return result, sum(measurements) / len(measurements), measurements

if __name__ == "__main__":
    for size in (1_000, 10_000, 200_000):
        items = [f"Item{i}:Rs{i % 50}" for i in range(size)]
        plus_text, plus_avg, plus_runs = average_time(build_plus, items)
        join_text, join_avg, join_runs = average_time(build_join, items)
        f_text, f_avg, f_runs = average_time(build_fstring, items)
        print(f"\\nLines: {size}")
        print("Same text:", plus_text == join_text == f_text)
        print(f"+= average:       {plus_avg:.6f} s | runs: {plus_runs}")
        print(f"join average:     {join_avg:.6f} s | runs: {join_runs}")
        print(f"f-string average: {f_avg:.6f} s | runs: {f_runs}")

# += can repeatedly create/copy strings because strings are immutable.
# join() is generally recommended for combining many pieces: O(n) total
# characters/time and O(total output size) memory. Repeated concatenation can
# require up to O(n^2) character copying in the general case. StringIO or
# writing line-by-line to a file can reduce the need to hold all pieces at once.
