"""
CP1404/CP5632 - Practical 03: simulate daily stock prices.
Start at $10.00. Each day has an equal chance of an increase of up to
17.5% or a decrease of up to 5%. Stop after the price moves outside
$1.00 to $100.00 and write the starting price and daily prices to a file.
"""

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "capitalist_conrad.txt"

price = INITIAL_PRICE
number_of_days = 0
out_file = open(FILENAME, "w")
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= 1 + price_change
    number_of_days += 1
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()
