"""CP1404/CP5632 - Practical 04: load and display subject information."""

FILENAME = "subject_data.txt"


def main():
    """Load the subject records and display their details."""
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename):
    """Return subject records as nested lists, with integer student counts."""
    subjects = []
    with open(filename, "r") as in_file:
        for line in in_file:
            subject_fields = line.strip().split(",")
            subject = [subject_fields[0], subject_fields[1], int(subject_fields[2])]
            subjects.append(subject)
    return subjects


def display_subjects(subjects):
    """Display subject codes, lecturer names and student counts."""
    for subject_code, lecturer, number_of_students in subjects:
        print(f"{subject_code} is taught by {lecturer:12} and has {number_of_students:3} students")


main()
