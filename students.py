"""Student data module: holds the student records and basic operations on them."""

students = [
    {"name": "Ada", "score": 91},
    {"name": "Tunde", "score": 58},
    {"name": "Chioma", "score": 76},
]


def add_student(name, score):
    """Add a new student record to the list."""
    students.append({"name": name, "score": score})


def average_score(data):
    """Return the average score, or 0 if the list is empty."""
    if len(data) == 0:
        return 0
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)