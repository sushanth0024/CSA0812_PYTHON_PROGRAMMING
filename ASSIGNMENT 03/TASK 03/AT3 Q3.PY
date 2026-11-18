
# Q3 - Dictionaries: Farmer Helpline Complaint Analysis

import random
import string
import time
from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}

# TODO 1: Count word frequencies using dictionary get()
def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower()
        words = words.translate(
            str.maketrans("", "", string.punctuation)
        )

        for word in words.split():
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts


# TODO 2: Find top k frequent words
def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]


print("Top frequent words:")
print(top(frequencies(calls, STOP), 3))

# Using setdefault()
def count_setdefault(texts, stop):
    result = {}

    for text in texts:
        for word in text.lower().split():
            if word not in stop:
                result.setdefault(word, 0)
                result[word] += 1

    return result


print("\nUsing setdefault:")
print(count_setdefault(calls, STOP))

# Group complaints by district
complaints = {
    "Kanchipuram": ["Seed delay", "Water shortage"],
    "Vellore": ["Fertiliser problem", "Crop disease"],
    "Chennai": ["Subsidy issue"]
}

print("\nComplaints by district:")

for district, items in complaints.items():
    print(district, ":", items)

# Group complaints by crop
crop_complaints = {}

records = [
    ("Rice", "Leaf disease"),
    ("Wheat", "Seed delay"),
    ("Rice", "Low market price")
]

for crop, complaint in records:
    crop_complaints.setdefault(crop, []).append(complaint)

print("\nComplaints by crop:")
print(crop_complaints)

# Dictionary views
result = frequencies(calls, STOP)

print("\nDictionary keys:", result.keys())
print("Dictionary values:", result.values())
print("Dictionary items:", result.items())

# Benchmark
print("\nBENCHMARK")

def generate_data(n):
    words = ["seeds", "water", "crop", "fertiliser", "price"]
    return [
        " ".join(random.choices(words, k=8))
        for _ in range(n)
    ]

for size in [1000, 10000, 100000]:

    data = generate_data(size)

    start = time.perf_counter()
    dictionary_result = frequencies(data, STOP)
    dictionary_time = time.perf_counter() - start

    start = time.perf_counter()
    counter_result = Counter(
        word
        for text in data
        for word in text.lower().split()
        if word not in STOP
    )
    counter_time = time.perf_counter() - start

    print("\nComplaints:", size)
    print("Dictionary time:", dictionary_time)
    print("Counter time:", counter_time)

    if size <= 10000:
        all_words = [
            word
            for text in data
            for word in text.lower().split()
            if word not in STOP
        ]

        start = time.perf_counter()
        list_result = {
            word: all_words.count(word)
            for word in set(all_words)
        }
        list_time = time.perf_counter() - start

        print("List count time:", list_time)

# Edge cases
print("\nEdge cases:")
print("Empty text:", frequencies([], STOP))
print("Upper/lower case:", frequencies(["SEEDS seeds"], STOP))

print("\nComplexity:")
print("Dictionary counting: O(n) average")
print("List count method: O(n*d)")
print("Dictionary space: O(d)")
print("Counter is another efficient frequency-counting method.")
