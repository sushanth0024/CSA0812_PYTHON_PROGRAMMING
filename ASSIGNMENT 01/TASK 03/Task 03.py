
# Named constants
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
BASE_FAT = 3.5
BASE_SNF = 8.5
MIN_FAT = 2.0
MAX_FAT = 7.0

# Variables
litres = 10
fat = 4.2
snf = 8.7

# Calculate milk rate
rate = BASE_RATE + ((fat - BASE_FAT) / 0.1) * FAT_STEP_VALUE
rate += ((snf - BASE_SNF) / 0.1) * SNF_STEP_VALUE

print("Milk Rate:", round(rate, 2))

# Dynamic typing
value = 10
print(type(value))
value = "Milk"
print(type(value))

# Multiple assignment and swapping
a, b = 10, 20
print("Before swapping:", a, b)

a, b = b, a
print("After swapping:", a, b)

# Dictionary alternative
RATE_CARD = {
    "base": 30.00,
    "fat": 0.40,
    "snf": 0.30
}

print("Dictionary Rate:", RATE_CARD["base"])
