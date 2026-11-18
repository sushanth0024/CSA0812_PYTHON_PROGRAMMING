
# Q6 - Nested Data: A Railway Timetable

import random
import time

# Timetable with five trains
timetable = {

    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:10"),
            ("Katpadi", "08:00", "08:05"),
            ("Bengaluru", "11:00", "11:10")
        ],
        "days": {"Mon", "Wed", "Fri"}
    },

    "12602": {
        "name": "Coastal Express",
        "stops": [
            ("Chennai", "07:00", "07:15"),
            ("Arakkonam", "08:30", "08:35"),
            ("Vellore", "10:00", "10:05")
        ],
        "days": {"Tue", "Thu", "Sat"}
    },

    "12603": {
        "name": "Hill Passenger",
        "stops": [
            ("Bengaluru", "05:30", "05:40"),
            ("Katpadi", "09:00", "09:05"),
            ("Chennai", "12:00", "12:10")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
    },

    "12604": {
        "name": "Southern Mail",
        "stops": [
            ("Chennai", "14:00", "14:10"),
            ("Vellore", "16:00", "16:05"),
            ("Bengaluru", "19:00", "19:10")
        ],
        "days": {"Sun"}
    },

    "12605": {
        "name": "City Link",
        "stops": [
            ("Arakkonam", "08:00", "08:05"),
            ("Katpadi", "09:30", "09:35"),
            ("Vellore", "10:30", "10:35")
        ],
        "days": {"Mon", "Fri"}
    }
}

# Find trains at a station on a given day
def find_trains(data, station, day):

    result = []

    for number, details in data.items():

        if day in details["days"]:

            for stop, arrival, departure in details["stops"]:

                if stop.lower() == station.lower():

                    result.append(
                        (departure, number, details["name"])
                    )

    return sorted(result, key=lambda x: x[0])


# Create station index
def create_index(data):

    index = {}

    for number, details in data.items():

        for station, arrival, departure in details["stops"]:

            index.setdefault(station.lower(), []).append(
                (number, details["name"], arrival, departure,
                 details["days"])
            )

    return index


# Search using index
def indexed_search(index, station, day):

    result = []

    for number, name, arrival, departure, days in index.get(station.lower(), []):

        if day in days:
            result.append((departure, number, name))

    return sorted(result, key=lambda x: x[0])


# Display timetable
print("RAILWAY TIMETABLE")

for number, details in timetable.items():

    print("\nTrain:", number)
    print("Name:", details["name"])
    print("Running days:", details["days"])

    for stop in details["stops"]:
        print(stop)

# Search
print("\nTrains stopping at Katpadi on Monday:")
print(find_trains(timetable, "Katpadi", "Mon"))

# Third station departure time
print("\nThird station departure:")
print(timetable["12601"]["stops"][2][2])

# Create index
index = create_index(timetable)

print("\nIndexed search:")
print(indexed_search(index, "Katpadi", "Mon"))

# Benchmark
print("\nBENCHMARK")

def generate_timetable(n):

    data = {}
    stations = ["Chennai", "Katpadi", "Bengaluru",
                "Vellore", "Arakkonam"]

    for i in range(n):

        chosen = random.sample(stations, 3)

        stops = [
            (station, "08:00", "08:05")
            for station in chosen
        ]

        data[str(20000 + i)] = {
            "name": "Train " + str(i),
            "stops": stops,
            "days": {"Mon", "Wed", "Fri"}
        }

    return data


for size in [100, 1000, 10000]:

    data = generate_timetable(size)

    start = time.perf_counter()
    normal = find_trains(data, "Katpadi", "Mon")
    normal_time = time.perf_counter() - start

    start = time.perf_counter()
    station_index = create_index(data)
    index_build_time = time.perf_counter() - start

    start = time.perf_counter()
    indexed = indexed_search(station_index, "Katpadi", "Mon")
    indexed_time = time.perf_counter() - start

    print("\nTrains:", size)
    print("Normal search:", normal_time)
    print("Index building:", index_build_time)
    print("Indexed search:", indexed_time)
    print("Same results:", normal == indexed)

# Edge cases
print("\nUnknown station:")
print(find_trains(timetable, "Unknown", "Mon"))

print("\nTrain not running on Monday:")
print(find_trains({"12604": timetable["12604"]}, "Chennai", "Mon"))

print("\nComplexity:")
print("Normal search: O(total stops)")
print("Indexed search: O(trains at station), plus sorting")
print("Index requires extra memory.")
