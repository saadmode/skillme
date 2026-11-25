import getpass
import os

# ---------- Load common passwords (stretch goal) ----------

def load_common_passwords(filename="common_passwords.txt"):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        print("Warning: common_passwords.txt not found. Skipping common-password check.")
        return set()


# ---------- Individual checks (each returns a score) ----------

def check_length(pw):
    if len(pw) >= 16:
        return 3
    elif len(pw) >= 12:
        return 2
    elif len(pw) >= 8:
        return 1
    return 0


def check_lowercase(pw):
    return 1 if any(c.islower() for c in pw) else 0


def check_uppercase(pw):
    return 1 if any(c.isupper() for c in pw) else 0


def check_digit(pw):
    return 1 if any(c.isdigit() for c in pw) else 0


def check_symbol(pw):
    return 1 if any(not c.isalnum() and not c.isspace() for c in pw) else 0


def is_common(pw, common):
    lowered = pw.lower()
    # Also catch tricks like "Password1!" by stripping trailing digits/symbols
    stripped = lowered.rstrip("0123456789!@#$%^&*?._-")
    return lowered in common or stripped in common


# ---------- Combine everything ----------

def rate_password(pw, common):
    """Returns (rating, tips). Never stores or prints the password."""
    tips = []

    if is_common(pw, common):
        return "Weak", ["This is a very common password (or a tiny variation of one). Pick something completely different."]

    score = 0
    score += check_length(pw)
    score += check_lowercase(pw)
    score += check_uppercase(pw)
    score += check_digit(pw)
    score += check_symbol(pw)

    # Tips for each missing rule
    if len(pw) < 12:
        tips.append("Make it at least 12 characters long (16+ is even better).")
    if not check_lowercase(pw):
        tips.append("Add at least one lowercase letter.")
    if not check_uppercase(pw):
        tips.append("Add at least one uppercase letter.")
    if not check_digit(pw):
        tips.append("Add at least one digit.")
    if not check_symbol(pw):
        tips.append("Add at least one symbol.")

    # Max score is 7. Short passwords can never be better than Weak.
    if len(pw) < 8 or score <= 3:
        rating = "Weak"
    elif score <= 5:
        rating = "Medium"
    else:
        rating = "Strong"

    return rating, tips


def main():
    print("=== PassGuard: Password Strength Checker ===")
    print("Only test your own passwords. Nothing is saved or shown.\n")

    common = load_common_passwords()

    while True:
        pw = getpass.getpass("Enter a password (or press Enter to quit): ")
        if pw == "":
            print("Bye!")
            break

        rating, tips = rate_password(pw, common)
        print(f"\nRating: {rating}")
        if tips:
            print("Tips:")
            for tip in tips:
                print(f"  - {tip}")
        else:
            print("No tips. Nice password!")
        print()


if __name__ == "__main__":
    main()