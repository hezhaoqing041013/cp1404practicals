"""CP1404/CP5632 - Practical 04: generate sorted, unique lottery picks."""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Ask how many quick picks to generate, then display each pick."""
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join([f"{number:2}" for number in quick_pick]))


def generate_quick_pick():
    """Return a sorted list of unique random numbers within the bounds."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


main()
