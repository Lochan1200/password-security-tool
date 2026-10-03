import bcrypt
import re
import getpass

def check_password_strength(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Add one lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        tips.append("Add one number")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        tips.append("Add one special character")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, tips

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return salt, hashed

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

password = getpass.getpass("Enter a password: ")

strength, tips = check_password_strength(password)

print("\nPassword Strength:", strength)

if tips:
    print("Suggestions:")
    for tip in tips:
        print("-", tip)

salt, hashed = hash_password(password)

print("\nSalt:", salt.decode())
print("Hashed Password:", hashed.decode())

again = getpass.getpass("\nEnter the same password again: ")

if verify_password(again, hashed):
    print("\nPassword verified successfully.")
else:
    print("\nPassword does not match.")