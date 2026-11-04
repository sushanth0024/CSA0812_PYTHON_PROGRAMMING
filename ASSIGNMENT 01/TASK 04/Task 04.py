
import math

fat = 4.2
snf = 8.7
litres = 10

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
amount = round(litres * rate, 2)

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre:", round(rate, 2))
print("Amount:", amount)

print("\nUnexpected results:")
print("0.1 + 0.2 =", 0.1 + 0.2)
print("-7 // 2 =", -7 // 2)
print("-2 ** 2 =", -2 ** 2)
print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)

print("\nRounding comparison:")
for f in [4.2, 3.1]:
    steps = (f - 3.5) / 0.1
    print("Fat:", f)
    print("round:", round(steps), "Rate:", 30 + round(steps) * 0.40)
    print("int:", int(steps), "Rate:", 30 + int(steps) * 0.40)
    print("floor:", math.floor(steps),
          "Rate:", 30 + math.floor(steps) * 0.40)

print("\nFat validation:", 2.0 <= fat <= 7.0)
print("Boolean condition:",
      2.0 <= fat <= 7.0 and 6.0 <= snf <= 10.0)
