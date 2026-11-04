
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP = Decimal("0.40")
SNF_STEP = Decimal("0.30")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")

def number(value):
    try:
        return Decimal(str(value).strip())
    except InvalidOperation:
        raise ValueError("Invalid number")

def calculate_payment(litres, fat, snf):
    litres = number(litres)
    fat = number(fat)
    snf = number(snf)

    if litres <= 0:
        raise ValueError("Quantity must be positive")
    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0")
    if not Decimal("6.0") <= snf <= Decimal("10.0"):
        raise ValueError("SNF must be between 6.0 and 10.0")

    fs = ((fat - BASE_FAT) / Decimal("0.1")).to_integral_value(
        rounding=ROUND_HALF_UP)
    ss = ((snf - BASE_SNF) / Decimal("0.1")).to_integral_value(
        rounding=ROUND_HALF_UP)

    rate = BASE_RATE + fs * FAT_STEP + ss * SNF_STEP
    rate = rate.quantize(Decimal("0.01"))
    return (litres * rate).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP)

# Automated test cases
tests = [
    ("Above standard", (8.5, 4.2, 8.7), "283.90"),
    ("Below standard", (12, 3.1, 8.3), "333.60"),
    ("Standard boundary", (10, 3.5, 8.5), "300.00"),
    ("Lowest fat", (10, 2.0, 8.5), "240.00"),
    ("Highest fat", (10, 7.0, 8.5), "440.00"),
    ("Text input", ("abc", 3.5, 8.5), "INVALID"),
    ("Negative quantity", (-5, 3.5, 8.5), "INVALID"),
    ("Fat below range", (10, 1.5, 8.5), "INVALID"),
    ("Fat above range", (10, 7.5, 8.5), "INVALID")
]

print("AUTOMATED TEST RESULTS")
for name, values, expected in tests:
    try:
        actual = calculate_payment(*values)
        assert actual == Decimal(expected)
        print(name, " : PASS - Rs.", actual)
    except ValueError:
        assert expected == "INVALID"
        print(name, " : PASS - Invalid input rejected")

# Five-entry calculation
farmers = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3),
    (5, 3.0, 8.0),
    (7.5, 4.0, 8.5)
]

total = Decimal("0.00")
print("\nFIVE-ENTRY PAYMENT DETAILS")

for litres, fat, snf in farmers:
    amount = calculate_payment(litres, fat, snf)
    total += amount
    print(litres, "L | Payment: Rs.", amount)

print("Ten-day total: Rs.", total)
assert total == Decimal("1290.00")
print("Five-entry total test: PASS")
