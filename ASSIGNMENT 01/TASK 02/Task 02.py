
from decimal import Decimal
import sys

# 1,000 payments of Rs 33.40 and three adjustments of Rs 0.10
payments = ["33.40"] * 1000 + ["0.10"] * 3

def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total

def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total

print("float :", total_float(payments))
print("Decimal:", total_decimal(payments))

print(0.1 + 0.2 == 0.3,
      Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

# Memory comparison
print("\nMemory usage:")
print("Float:", sys.getsizeof(10.0), "bytes")
print("Integer:", sys.getsizeof(10), "bytes")
print("Decimal:", sys.getsizeof(Decimal("10.0")), "bytes")
