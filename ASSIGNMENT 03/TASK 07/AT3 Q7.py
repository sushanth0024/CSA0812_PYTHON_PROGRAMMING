
# Q7 - Design a Contact-Merging Program

import random
import time

# Normalize phone number
def normalize_phone(phone):

    if not phone:
        return ""

    digits = ""

    for ch in str(phone):
        if ch.isdigit():
            digits += ch

    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    return digits


# Normalize name
def normalize_name(name):

    if not name:
        return ""

    return " ".join(name.lower().strip().split())


# Merge contacts using dictionary
def merge_contacts(contacts):

    merged = {}

    for contact in contacts:

        phone = normalize_phone(contact.get("phone", ""))
        name = contact.get("name", "").strip()
        email = contact.get("email", "").strip().lower()

        # Skip contacts without phone numbers
        if not phone:
            continue

        if phone not in merged:

            merged[phone] = {
                "name": name,
                "numbers": set(),
                "emails": set(),
                "name_variants": set()
            }

        if name:
            merged[phone]["name_variants"].add(name)

            if not merged[phone]["name"]:
                merged[phone]["name"] = name

        merged[phone]["numbers"].add(phone)

        if email:
            merged[phone]["emails"].add(email)

    return merged


# Sample contacts
contacts = [

    {
        "name": "Dr. Ravi",
        "phone": "+91 98400 12345",
        "email": "RAVI@MAIL.COM"
    },

    {
        "name": "ravi kumar",
        "phone": "9840012345",
        "email": "ravi.work@mail.com"
    },

    {
        "name": "Anu",
        "phone": "9000011111",
        "email": "anu@mail.com"
    },

    {
        "name": "Ravi",
        "phone": "",
        "email": "unknown@mail.com"
    },

    {
        "name": "Different Ravi",
        "phone": "9000099999",
        "email": ""
    }
]

print("ORIGINAL CONTACTS")

for contact in contacts:
    print(contact)

# Merge
merged_contacts = merge_contacts(contacts)

print("\nMERGED CONTACTS")

for phone, details in merged_contacts.items():

    print("\nPhone:", phone)
    print("Name:", details["name"])
    print("Numbers:", details["numbers"])
    print("Emails:", details["emails"])
    print("Name variants:", details["name_variants"])


# Benchmark
def generate_contacts(n):

    data = []

    for i in range(n):

        person = i // 2

        phone = "98400" + str(person % 100000).zfill(5)

        if i % 2:
            phone = "+91 " + phone[:5] + " " + phone[5:]

        data.append({
            "name": "Person " + str(person),
            "phone": phone,
            "email": "person" + str(person) + "@mail.com"
        })

    return data


print("\nBENCHMARK")

for size in [1000, 100000]:

    data = generate_contacts(size)

    start = time.perf_counter()
    result = merge_contacts(data)
    elapsed = time.perf_counter() - start

    print("\nContacts:", size)
    print("Dictionary merging time:", elapsed)
    print("Unique groups:", len(result))


# Small hand verification
small_contacts = [
    {"name": "Ravi", "phone": "9840012345", "email": "ravi@mail.com"},
    {"name": "Ravi Kumar", "phone": "+91 98400 12345", "email": "rk@mail.com"}
]

small_result = merge_contacts(small_contacts)

print("\nHAND VERIFICATION")
print(small_result)


print("\nDESIGN EXPLANATION")
print("Input: Contact records from different devices.")
print("Output: Merged contacts with unique numbers and emails.")
print("Dictionary: Groups contacts using normalized phone numbers.")
print("Sets: Remove duplicate phone numbers and emails.")
print("Same name with different numbers remains separate.")
print("Missing phone numbers are skipped.")
print("Limitation: Shared phone numbers may merge different people.")

print("\nCOMPLEXITY")
print("Dictionary merging: O(n) average time.")
print("Pairwise comparison: O(n^2) time.")
print("Dictionary storage: O(n) space.")
