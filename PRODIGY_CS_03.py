import re


def password_strength(password):
    # Initialize score
    score = 0

    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Evaluate criteria and update score
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    # Feedback for improvement
    feedback = []
    if not length_criteria:
        feedback.append("Increase the password length to at least 8 characters.")
    if not uppercase_criteria:
        feedback.append("Add at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Add at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Include at least one number.")
    if not special_char_criteria:
        feedback.append("Use at least one special character (e.g., !@#$%^&*).")

    return strength, feedback


# Example usage
password = input("Enter a password to check its strength: ")
strength, feedback = password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions to improve your password:")
    for suggestion in feedback:
        print(f"- {suggestion}")