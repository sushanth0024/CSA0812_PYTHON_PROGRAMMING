
from decimal import Decimal, ROUND_HALF_UP
from time import perf_counter

# Five sample farmer payments
payment_values = ["300.00", "283.90", "333.60", "132.50", "240.00"]

print("1. FLOAT AND DECIMAL COMPARISON")

for size in [300, 6000, 150000]:
    payments = payment_values * (size // 5)

    start = perf_counter()
    float_total = sum(float(x) for x in payments)
    float_time = perf_counter() - start

    start = perf_counter()
    decimal_total = sum(Decimal(x) for x in payments)
    decimal_time = perf_counter() - start

    difference = Decimal(str(float_total)) - decimal_total

    print("\nPayments:", size)
    print("Float total:", float_total)
    print("Decimal total:", decimal_total)
    print("Difference:", difference)
    print("Float time:", round(float_time, 6), "seconds")
    print("Decimal time:", round(decimal_time, 6), "seconds")


print("\n2. ROUNDING COMPARISON")

values = [Decimal("10.005")] * 3

each_rounded = sum(
    x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    for x in values
)

total_rounded = sum(values).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP
)

print("Round each payment:", each_rounded)
print("Round final total:", total_rounded)


print("\n3. DICTIONARY RATE TABLE COMPARISON")

BASE = Decimal("30.00")
FAT_VALUE = Decimal("0.40")
SNF_VALUE = Decimal("0.30")

def calculate_rate(fat, snf):
    fat_steps = ((fat - Decimal("3.5")) / Decimal("0.1"))
    snf_steps = ((snf - Decimal("8.5")) / Decimal("0.1"))

    fat_steps = fat_steps.to_integral_value(rounding=ROUND_HALF_UP)
    snf_steps = snf_steps.to_integral_value(rounding=ROUND_HALF_UP)

    return BASE + fat_steps * FAT_VALUE + snf_steps * SNF_VALUE

records = [
    (Decimal("3.5"), Decimal("8.5")),
    (Decimal("4.2"), Decimal("8.7")),
    (Decimal("3.1"), Decimal("8.3")),
    (Decimal("3.0"), Decimal("8.0")),
    (Decimal("4.0"), Decimal("8.5"))
] * 30000

start = perf_counter()
for fat, snf in records:
    rate = calculate_rate(fat, snf)
uncached_time = perf_counter() - start

rate_table = {}
start = perf_counter()

for fat, snf in records:
    key = (fat, snf)

    if key not in rate_table:
        rate_table[key] = calculate_rate(fat, snf)

    rate = rate_table[key]

cached_time = perf_counter() - start

print("Number of records:", len(records))
print("Unique rate combinations:", len(rate_table))
print("Without dictionary:", round(uncached_time, 6), "seconds")
print("With dictionary:", round(cached_time, 6), "seconds")
