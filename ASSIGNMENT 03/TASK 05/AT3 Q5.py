
# Q5: Cleaning Sensor Readings

# 1. Sensor readings
readings = [25, 30, 55, -60, 5, 8, 45, 70, -10, 100]

print("Original Readings:", readings)

# 2. Remove invalid readings (-50 to 50)
valid = [x for x in readings if -50 <= x <= 50]
print("\nValid Readings:", valid)

# 3. Invalid readings
invalid = [x for x in readings if x < -50 or x > 50]
print("Invalid Readings:", invalid)

# 4. Celsius to Fahrenheit
fahrenheit = [(x * 9/5) + 32 for x in valid]
print("Fahrenheit:", fahrenheit)

# 5. Alarm readings outside 2 to 8 degrees
alarms = [x for x in readings if x < 2 or x > 8]
print("Alarm Readings:", alarms)

# 6. Using normal loop
loop_result = []
for x in readings:
    if -50 <= x <= 50:
        loop_result.append(x)

print("\nUsing Loop:", loop_result)

# 7. Using map()
converted = list(map(lambda x: x * 9/5 + 32, valid))
print("Using map():", converted)

# 8. Using filter()
filtered = list(filter(lambda x: -50 <= x <= 50, readings))
print("Using filter():", filtered)

# 9. Dictionary comprehension
temperature_dict = {x: round(x * 9/5 + 32, 2) for x in valid}
print("\nTemperature Dictionary:", temperature_dict)

# 10. Set comprehension
temperature_set = {x for x in readings if -50 <= x <= 50}
print("Temperature Set:", temperature_set)

# 11. Generator expression
generator = (x for x in valid)
print("\nGenerator Values:", list(generator))

# 12. Edge cases
empty = []
print("\nEmpty List:", [x for x in empty if x > 0])

short = [5, 60]
print("Short List:", [x for x in short if -50 <= x <= 50])
