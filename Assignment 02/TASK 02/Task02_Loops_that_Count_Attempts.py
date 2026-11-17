# Q2 - Loops that Count Attempts
# Demo OTP is 2468. Blank entries do not use an attempt.

CORRECT_OTP = "2468"

def verify_with_while():
    print("\\nWHILE LOOP")
    attempts = 0
    while attempts < 3:
        otp = input("Enter OTP (blank to skip): ").strip()
        if otp == "":
            print("Blank entry: attempt not counted.")
            continue
        attempts += 1
        if otp == CORRECT_OTP:
            print("OTP verified.")
            break
        print("Incorrect OTP. Attempts used:", attempts)
    else:
        print("Account locked for 30 minutes.")

def verify_with_for():
    print("\\nFOR LOOP")
    attempts = 0
    for _ in range(3):
        otp = input("Enter OTP (blank to skip): ").strip()
        if otp == "":
            print("Blank entry: attempt not counted.")
            # A for-loop still advances its iteration after continue.
            # Use a while loop if blank entries must not consume a slot.
            continue
        attempts += 1
        if otp == CORRECT_OTP:
            print("OTP verified.")
            break
        print("Incorrect OTP. Attempts used:", attempts)
    else:
        print("Account locked for 30 minutes.")

def verify_with_for_counted_attempts():
    """For-loop version where blank input does not consume an attempt."""
    print("\\nFOR LOOP (blank-safe)")
    attempts = 0
    for _ in range(3):
        while True:
            otp = input("Enter OTP (blank to skip): ").strip()
            if otp:
                break
            print("Blank entry: attempt not counted.")
        attempts += 1
        if otp == CORRECT_OTP:
            print("OTP verified.")
            break
        print("Incorrect OTP. Attempts used:", attempts)
    else:
        print("Account locked for 30 minutes.")

def recursive_verify(remaining=3):
    """Recursive alternative; each nonblank wrong OTP uses one attempt."""
    if remaining == 0:
        print("Account locked for 30 minutes.")
        return
    otp = input("Enter OTP (blank to skip): ").strip()
    if not otp:
        print("Blank entry: attempt not counted.")
        return recursive_verify(remaining)
    if otp == CORRECT_OTP:
        print("OTP verified.")
        return
    print("Incorrect OTP.")
    return recursive_verify(remaining - 1)

def demonstrate_pass():
    # pass is a placeholder: it performs no action.
    security_question_verified = False
    if security_question_verified:
        pass  # Add extra-attempt handling here when implemented.
    print("pass demonstration completed.")

if __name__ == "__main__":
    print("Choose 1=while, 2=for blank-safe, 3=recursive, 4=pass demo")
    choice = input("Choice: ").strip()
    if choice == "1":
        verify_with_while()
    elif choice == "2":
        verify_with_for_counted_attempts()
    elif choice == "3":
        recursive_verify()
    elif choice == "4":
        demonstrate_pass()
    else:
        print("Invalid choice.")

# Changed condition: after correct security-question verification, set the
# allowed-attempt count to 5 instead of 3. Keep the attempt counter separate
# from blank entries. Loop time is O(a), loop extra space O(1);
# recursion time and call-stack space are O(a).
