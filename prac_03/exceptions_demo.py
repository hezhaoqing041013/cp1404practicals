"""CP1404/CP5632 - Practical 03: handle invalid division input."""

# 1. ValueError occurs when int() cannot convert an input string to an
# integer, for example, "hello", "1.5" or an empty string.
# 2. In the original code, ZeroDivisionError occurs if the denominator is 0.
# 3. Yes. Check the denominator and re-prompt while it is 0 before dividing.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
