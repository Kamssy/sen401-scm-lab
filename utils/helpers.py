"""Utility functions for working with student records."""


def highest_score(data):
    """Return the student with the highest score, or None if empty."""
    if not data:
        return None
    return max(data, key=lambda s: s["score"])


def lowest_score(data):
    """Return the student with the lowest score, or None if empty."""
    if not data:
        return None
    return min(data, key=lambda s: s["score"])