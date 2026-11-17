# Q1 - Decisions with Many Boundaries
# Electricity subsidy eligibility

households = [
    (1001, 100, False, False),
    (1002, 100, True, False),
    (1003, 101, True, False),
    (1004, 101, False, False),
    (1005, 200, True, False),
    (1006, 200, False, False),
    (1007, 201, False, False),
    (1008, 250, False, True)
]

def separate_if_decision(units, ration_card, elderly):
    results = []
    if units <= 100:
        results.append("Full subsidy")
    if 101 <= units <= 200 and ration_card:
        results.append("Partial subsidy")
    if units > 200 and not elderly:
        results.append("No subsidy")
    if units > 200 and elderly:
        results.append("Special subsidy")
    if not results:
        results.append("No subsidy")
    return " + ".join(results)

def elif_decision(units, ration_card, elderly):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        else:
            return "No subsidy"
    elif units > 200:
        if elderly:
            return "Special subsidy"
        else:
            return "No subsidy"

print("ID     Units  Ration  Elderly  Separate-if result       if-elif-else result")
for cid, units, ration, elderly in households:
    print(f"{cid:<6} {units:<6} {str(ration):<7} {str(elderly):<8} "
          f"{separate_if_decision(units, ration, elderly):<25} "
          f"{elif_decision(units, ration, elderly)}")

# Alternative: lookup table / match-case can also be used.
# With k slabs, a sequential lookup takes O(k) time and O(k) table space.
# An if-elif chain takes O(k) worst-case time and O(1) extra space.
