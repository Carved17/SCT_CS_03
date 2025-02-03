import re

class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password

    def check_strength(self):
        """
        Checks the strength of the password based on various criteria.

        Returns:
            A string indicating the password strength (e.g., "Weak", "Medium", "Strong")
            and a list of suggestions for improvement.
        """

        score = 0
        suggestions = []

        # Check length
        if len(self.password) >= 8:
            score += 1
        else:
            suggestions.append("Password should be at least 8 characters long.")

        # Check for uppercase letters
        if any(c.isupper() for c in self.password):
            score += 1
        else:
            suggestions.append("Include at least one uppercase letter.")

        # Check for lowercase letters
        if any(c.islower() for c in self.password):
            score += 1
        else:
            suggestions.append("Include at least one lowercase letter.")

        # Check for digits
        if any(c.isdigit() for c in self.password):
            score += 1
        else:
            suggestions.append("Include at least one digit.")

        # Check for special characters
        special_chars = "!@#$%^&*()-_=+[]{};:,.<>/?"
        if any(c in special_chars for c in self.password):
            score += 1
        else:
            suggestions.append("Include at least one special character.")

        # Determine strength based on score
        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        else:
            strength = "Strong"

        return strength, suggestions

if __name__ == "__main__":
    password = input("Enter the password: ")
    checker = PasswordStrengthChecker(password)
    strength, suggestions = checker.check_strength()

    print(f"Password strength: {strength}")
    if strength != "Strong":
        print("Suggestions for improvement:")
        for suggestion in suggestions:
            print(f"- {suggestion}")