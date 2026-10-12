"""CP1404/CP5632 - Practical 03: keep asking until an integer is entered."""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Valid result is: {result}")
