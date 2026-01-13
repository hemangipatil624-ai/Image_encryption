def check_password(password):
    strength = 0
    feedback = []

    # Length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Uppercase
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter")

    # Lowercase
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter")

    # Number
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Include at least one number")

    # Special character
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    if any(char in special_chars for char in password):
        strength += 1
    else:
        feedback.append("Include at least one special character")

    # Determine rating
    if strength == 5:
        rating = "Very Strong"
    elif strength == 4:
        rating = "Strong"
    elif strength == 3:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, feedback

# -------------------------------
# Take password input from user
password = input("Enter your password: ")

# Check password strength
rating, feedback = check_password(password)

# Display results
print("\nPassword Strength:", rating)
if feedback:
    print("Suggestions to improve your password:")
    for f in feedback:
        print("-", f)
