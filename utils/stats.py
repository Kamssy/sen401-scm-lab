from statistics import median
from students import Student

def average_score(data: list[Student]) -> float:
    """Return the average score, or 0 if the list is empty."""
    if not data:
        return 0
    return sum(s.score for s in data) / len(data)


def median_score(data: list[Student]) -> float:
    """Return the median score, or 0 if the list is empty."""
    if not data:
        return 0
    return median([s.score for s in data])