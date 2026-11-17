# Q3 - Vehicle Registration Number Validator
# Valid format: 2 state letters + 2 district digits + 1/2 series letters + 4 digits.

def normalise(text):
    """Remove spaces/hyphens and convert to uppercase."""
    return text.strip().replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    """Validate using slicing and string methods only."""
    if len(reg) not in (9, 10):
        return False
    if not reg[0:2].isalpha():
        return False
    if not reg[2:4].isdigit():
        return False
    if len(reg) == 9:
        series = reg[4:5]
        number = reg[5:9]
    else:
        series = reg[4:6]
        number = reg[6:10]
    return series.isalpha() and number.isdigit()

def format_reg(reg):
    """Format a valid registration as TN 09 AB 1234."""
    if not is_valid(reg):
        return "INVALID"
    state = reg[0:2]
    district = reg[2:4]
    if len(reg) == 9:
        series = reg[4:5]
        number = reg[5:9]
    else:
        series = reg[4:6]
        number = reg[6:10]
    return state + " " + district + " " + series + " " + number

if __name__ == "__main__":
    samples = [
        "tn 09 ab 1234",
        "KA-01-M-0007",
        "TN9AB1234",
        "TN 22 1234 AB",
        "AP 39 C 5678",
        "MH-12-DE-12345"
    ]
    for raw in samples:
        reg = normalise(raw)
        status = "valid" if is_valid(reg) else "INVALID"
        print(f"{raw:18} -> {reg:11} {status:7} Receipt: {format_reg(reg)}")

# Strings are immutable: methods return new strings rather than changing the
# original. text.upper() returns an uppercase copy; assign it to keep it.
# s[-4:] gives the final four characters. For a 9-character string,
# s[4:-4] gives one character; for a 10-character string, it gives two.
# Complexity: normalisation and validation are O(L) time; O(L) space for
# the resulting normalised string. A regular expression fullmatch is also O(L).
