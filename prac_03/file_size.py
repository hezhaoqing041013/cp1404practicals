"""CP1404/CP5632 - Practical 03: count lines in files chosen by the user."""


def main():
    """Ask for filenames and report line counts or missing-file errors."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            number_of_lines = get_number_of_lines(filename)
            print(f"{filename} has {number_of_lines} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")


def get_number_of_lines(filename):
    """Return the number of lines in a file, allowing file errors to propagate."""
    number_of_lines = 0
    with open(filename, "r") as in_file:
        for line in in_file:
            number_of_lines += 1
    return number_of_lines


main()
