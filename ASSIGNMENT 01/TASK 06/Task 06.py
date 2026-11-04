
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    """Calculate milk rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE
                 + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    """Calculate payment for one farmer."""
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(records):
    """Calculate total payment for all farmer records."""
    total = 0
    for litres, fat, snf in records:
        total += payout(litres, fat, snf)
    return round(total, 2)

# Farmer records: litres, fat, SNF
farmers = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3)
]

for litres, fat, snf in farmers:
    rate = rate_per_litre(fat, snf)
    amount = payout(litres, fat, snf)
    print(f"{litres} L | Rate: Rs.{rate:.2f} | Payment: Rs.{amount:.2f}")

print("10-day total: Rs.", ten_day_total(farmers))
