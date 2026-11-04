
def read_number(message):
    while True:
        text = input(message)

        try:
            return float(text.strip())
        except ValueError:
            print("Invalid input! Enter a valid number.")

litres = read_number("Enter litres: ")
fat = read_number("Enter fat percentage: ")
snf = read_number("Enter SNF percentage: ")

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
amount = round(litres * rate, 2)

print("\n--- MILK PAYMENT DETAILS ---")
print(f"Litres:       {litres:8.2f}")
print(f"Fat:          {fat:8.2f}")
print(f"SNF:          {snf:8.2f}")
print(f"Rate:         Rs. {rate:8.2f}")
print(f"Total Amount: Rs. {amount:8.2f}")
