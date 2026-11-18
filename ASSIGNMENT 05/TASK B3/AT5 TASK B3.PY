
import csv
import io
import sqlite3
import time
import cProfile
from collections import defaultdict

def generate_data(stations, days=30):
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["station", "date", "pm25"])

    for s in range(stations):
        for d in range(days):
            for h in range(24):
                station = "Station" + str(s + 1)
                date = "2026-01-" + str(d + 1).zfill(2)
                pm25 = 30 + (s * 2) + (h % 20)
                writer.writerow([station, date, pm25])

    return output.getvalue()


def python_method(text):
    data = defaultdict(list)
    reader = csv.DictReader(io.StringIO(text))

    for row in reader:
        key = (row["station"], row["date"])
        data[key].append(float(row["pm25"]))

    return {
        key: sum(values) / len(values)
        for key, values in data.items()
    }


def sql_method(text):
    con = sqlite3.connect(":memory:")

    con.execute(
        "CREATE TABLE readings (station TEXT, day TEXT, pm25 REAL)"
    )

    reader = csv.DictReader(io.StringIO(text))
    rows = [
        (r["station"], r["date"], float(r["pm25"]))
        for r in reader
    ]

    con.executemany(
        "INSERT INTO readings VALUES (?, ?, ?)", rows
    )

    result = con.execute("""
        SELECT station, day, AVG(pm25)
        FROM readings
        GROUP BY station, day
    """).fetchall()

    con.close()
    return result


def profile_python():
    sample = generate_data(1, 30)
    python_method(sample)


for stations in [1, 12, 120]:
    data = generate_data(stations, 365)

    start = time.perf_counter()
    result1 = python_method(data)
    python_time = time.perf_counter() - start

    start = time.perf_counter()
    result2 = sql_method(data)
    sql_time = time.perf_counter() - start

    print("\nStations:", stations)
    print("Readings:", stations * 365 * 24)
    print("Python loop time:", round(python_time, 4), "seconds")
    print("SQL time:", round(sql_time, 4), "seconds")
    print("Daily groups:", len(result1))
    print("Results agree:", len(result1) == len(result2))

print("\nProfiling Python method:")
cProfile.run("profile_python()")
