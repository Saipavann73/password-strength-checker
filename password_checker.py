import re


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    common_passwords = [
        "password",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "letmein"
    ]

    if password.lower() in common_passwords:
        score = 0
        feedback.append("Avoid commonly used passwords.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


print("=== Password Strength Checker ===")

password = input("Enter your password: ")

strength, feedback = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("- " + item)
else:
    print("Excellent! Your password meets all the basic requirements.")
