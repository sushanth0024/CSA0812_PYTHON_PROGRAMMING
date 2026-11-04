
from decimal import Decimal, ROUND_HALF_UP

BONUS_RATE = Decimal("0.50")
BONUS_LIMIT = Decimal("500")

def get_rate_card(month):
    if month in [4, 5, 6]:
        return Decimal("32.00"), Decimal("0.45"), Decimal("0.30")
    return Decimal("30.00"), Decimal("0.40"), Decimal("0.30")

def calculate_rate(fat, snf, month):
    base, fat_value, snf_value = get_rate_card(month)

    fat_steps = ((fat - Decimal("3.5")) / Decimal("0.1"))
    snf_steps = ((snf - Decimal("8.5")) / Decimal("0.1"))

    fat_steps = fat_steps.to_integral_value(rounding=ROUND_HALF_UP)
    snf_steps = snf_steps.to_integral_value(rounding=ROUND_HALF_UP)

    rate = base + fat_steps * fat_value + snf_steps * snf_value
    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def calculate_bonus(total_litres):
    if total_litres > BONUS_LIMIT:
        return total_litres * BONUS_RATE
    return Decimal("0.00")

def ten_day_payment(records, month):
    total_litres = Decimal("0.00")
    total_payment = Decimal("0.00")

    for litres, fat, snf in records:
        litres = Decimal(str(litres))
        fat = Decimal(str(fat))
        snf = Decimal(str(snf))

        if litres <= 0:
            raise ValueError("Litres must be positive")
        if not Decimal("2.0") <= fat <= Decimal("7.0"):
            raise ValueError("Invalid fat value")
        if not Decimal("6.0") <= snf <= Decimal("10.0"):
            raise ValueError("Invalid SNF value")

        rate = calculate_rate(fat, snf, month)
        total_litres += litres
        total_payment += litres * rate

    bonus = calculate_bonus(total_litres)
    final_payment = (total_payment + bonus).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

    return total_litres, bonus, final_payment


# TEST 1: Seasonal rate comparison
fat = Decimal("4.25")
snf = Decimal("8.63")

print("SEASONAL RATE TESTS")
print("April-June rate:", calculate_rate(fat, snf, 4))
print("Other month rate:", calculate_rate(fat, snf, 1))

# TEST 2: Bonus threshold tests
print("\nBONUS TESTS")
for litres in ["499", "500", "501", "600"]:
    bonus = calculate_bonus(Decimal(litres))
    print(litres, "litres -> Bonus Rs.", bonus)

# TEST 3: Ten-day payment
print("\nTEN-DAY PAYMENT TESTS")

records = [(501, 4.25, 8.63)]

for month, label in [(4, "April-June"), (1, "Other months")]:
    litres, bonus, payment = ten_day_payment(records, month)
    print(label)
    print("Total litres:", litres)
    print("Bonus:", bonus)
    print("Final payment:", payment)

# AUTOMATED ASSERTION TESTS
assert calculate_rate(fat, snf, 4) == Decimal("35.90")
assert calculate_rate(fat, snf, 1) == Decimal("33.50")
assert calculate_bonus(Decimal("500")) == Decimal("0.00")
assert calculate_bonus(Decimal("501")) == Decimal("250.50")

assert ten_day_payment([(500, 4.25, 8.63)], 4)[2] == Decimal("17950.00")
assert ten_day_payment([(501, 4.25, 8.63)], 4)[2] == Decimal("18236.40")
assert ten_day_payment([(501, 4.25, 8.63)], 1)[2] == Decimal("17034.00")

print("\nAll tests passed!")
