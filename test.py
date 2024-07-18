from unittest.mock import patch


# Function that reads input
def read_input():
    return input("Enter something: ")


# Mocking input for testing
with patch("builtins.input", side_effect=["Test input"]):
    user_input = read_input()

print(f"You entered: {user_input}")
