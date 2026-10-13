"""CP1404/CP5632 - Practical 04: list indexing, slicing and membership."""

numbers = [3, 1, 4, 1, 5, 9, 2]

# Expected values for the ORIGINAL list (before the changes below):
# numbers[0]          -> 3
# numbers[-1]         -> 2
# numbers[3]          -> 1
# numbers[:-1]        -> [3, 1, 4, 1, 5, 9]
# numbers[3:4]        -> [1]
# 5 in numbers       -> True
# 7 in numbers       -> False
# "3" in numbers     -> False
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1. Change the first element to the string "ten".
numbers[0] = "ten"

# 2. Change the last element to 1.
numbers[-1] = 1

# 3. Print every element except the first two.
print(numbers[2:])

# 4. Print whether 9 is an element of the list.
print(9 in numbers)
