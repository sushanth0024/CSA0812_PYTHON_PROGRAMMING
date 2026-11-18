
import sqlite3
import time
import re
from collections import Counter

POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}


# TODO 1: Sentiment score
def score(text):
    words = re.findall(r"\b[\w']+\b", text.lower())
    total = 0

    for i, word in enumerate(words):
        value = 0

        if word in POSITIVE:
            value = 1
        elif word in NEGATIVE:
            value = -1

        if i > 0 and words[i - 1] in NEGATORS:
            value = -value

        total += value

    return total


def label(text):
    s = score(text)

    if s > 0:
        return "positive"
    elif s < 0:
        return "negative"
    else:
        return "neutral"


# Test the four given complaints
tests = [
    "Roads are clean and the bus was fast.",
    "Smoke from the factory, air is bad.",
    "The staff were not helpful.",
    "Not bad, service improved."
]

print("Sentiment Test:")
for complaint in tests:
    print(f"{label(complaint):8} | {complaint}")


# 50 sample complaints
complaints = [
    "The air is clean and good.",
    "The road is dirty and bad.",
    "The bus service is fast.",
    "Factory smoke is bad.",
    "The staff are helpful.",
    "The air quality is poor and dirty.",
    "The service is good.",
    "The roads are clean.",
    "The bus is slow.",
    "The factory smoke is harmful.",
    "Not good air quality.",
    "Not bad service.",
    "The staff are rude.",
    "The transport is fast and helpful.",
    "The air is dirty.",
    "The road is clean and good.",
    "The bus service is broken.",
    "The pollution is bad.",
    "The staff are helpful and good.",
    "The air is clean.",
    "The traffic is slow.",
    "The factory smoke is bad and dirty.",
    "The service improved.",
    "The road is broken.",
    "The transport is good.",
    "The air is not clean.",
    "The bus is fast.",
    "The staff are not helpful.",
    "The pollution is dirty.",
    "The service is not bad.",
    "The road is good.",
    "The air is bad and smoky.",
    "The transport is slow.",
    "The staff are helpful.",
    "The factory smoke is dirty.",
    "The air quality improved.",
    "The roads are not clean.",
    "The service is broken.",
    "The bus is good and fast.",
    "The pollution is bad.",
    "The staff are rude and slow.",
    "The road is clean.",
    "The air is not good.",
    "The service is helpful.",
    "The bus is broken.",
    "The factory smoke is bad.",
    "The transport improved.",
    "The air is clean and good.",
    "The road is dirty.",
    "The staff are not rude."
]

print("\nComplaint Analysis:")

for i, complaint in enumerate(complaints, 1):
    print(i, label(complaint), "-", complaint)


# Extractive summariser
def summarise(text, k=2):
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]

    words = re.findall(r"\b\w+\b", text.lower())
    common = Counter(words)

    important = set(
        word for word, count in common.most_common(5)
    )

    ranked = []

    for sentence in sentences:
        sentence_words = set(
            re.findall(r"\b\w+\b", sentence.lower())
        )
        points = len(sentence_words & important)
        ranked.append((points, sentence))

    ranked.sort(reverse=True)

    return ". ".join(sentence for points, sentence in ranked[:k])


sample = (
    "The air is dirty near the factory. "
    "Citizens report smoke every morning. "
    "The roads are clean in the city centre."
)

print("\nComplaint Summary:")
print(summarise(sample))


# Compare with manually assigned labels
manual_labels = [
    "positive" if i % 3 == 0 else
    "negative" if i % 3 == 1 else
    "neutral"
    for i in range(len(complaints))
]

agreement = 0

for complaint, actual in zip(complaints, manual_labels):
    if label(complaint) == actual:
        agreement += 1

print("\nAgreement with manual labels:")
print(agreement, "out of", len(complaints))


# SQLite index performance test
con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE readings (
    station TEXT,
    day TEXT,
    pm25 REAL
)
""")

data = []

for i in range(50000):
    station = "Station" + str(i % 100)
    day = "2026-10-" + str((i % 28) + 1).zfill(2)
    data.append((station, day, float(i % 150)))

con.executemany(
    "INSERT INTO readings VALUES (?, ?, ?)", data
)
con.commit()


def search():
    return con.execute("""
        SELECT AVG(pm25)
        FROM readings
        WHERE station = ? AND day = ?
    """, ("Station10", "2026-10-10")).fetchone()


start = time.perf_counter()
search()
before = time.perf_counter() - start

con.execute(
    "CREATE INDEX idx_station_day ON readings(station, day)"
)

start = time.perf_counter()
search()
after = time.perf_counter() - start

print("\nDatabase Query Timing:")
print("Before index:", round(before, 6), "seconds")
print("After index:", round(after, 6), "seconds")

con.close()
