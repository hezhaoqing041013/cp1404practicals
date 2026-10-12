"""CP1404/CP5632 - Practical 03: explore random-number functions."""

import random

# 1. randint returns an integer from 5 to 20, inclusive.
# Example observations from a test run: 17, 9, 19.
# Smallest possible value: 5. Largest possible value: 20.
print(random.randint(5, 20))

# 2. randrange selects from 3, 5, 7 and 9 (10 is excluded).
# Example observations from a test run: 9, 5, 5.
# Smallest possible value: 3. Largest possible value: 9.
# It cannot produce 4 because the sequence starts at 3 and steps by 2.
print(random.randrange(3, 10, 2))

# 3. uniform returns a floating-point number between 2.5 and 5.5.
# Example observations from a test run: 3.2188078007120033,
# 3.2135134883827123 and 5.055739400339739.
# Lower bound: 2.5. Upper bound: 5.5.
# The upper endpoint may or may not occur because of float rounding.
print(random.uniform(2.5, 5.5))

# 4. Generate an integer from 1 to 100, including both endpoints.
print(random.randint(1, 100))
