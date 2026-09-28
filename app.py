from pydantic import ValidationError
from students import students, add_student
from utils.helpers import highest_score, lowest_score
from utils.stats import average_score, median_score

def print_table(data) -> None:
    """Print students ranked by score in an aligned table."""
    print(f"{'Rank':<6}{'Name':<12}{'Score':>6}")
    print("-" * 24)
    ranked = sorted(data, key=lambda s: s.score, reverse=True)
    for rank, s in enumerate(ranked, start=1):
        print(f"{rank:<6}{s.name:<12}{s.score:>6.1f}")

def main() -> None:
    print("=== Student Records Demo ===")
    add_student("Ngozi", 74)

    try:
        add_student("Bad Entry", 150)
    except ValidationError as err:
        print(f"Rejected invalid student: {err.errors()[0]['msg']}")

    if not students:
        print("No students recorded yet.")
        return

    print()
    print_table(students)
    print()
    print(f"Average score: {average_score(students):.2f}")
    print(f"Median score:  {median_score(students):.2f}")
    top = highest_score(students)
    bottom = lowest_score(students)
    print(f"Highest: {top.name} ({top.score:.1f})")
    print(f"Lowest:  {bottom.name} ({bottom.score:.1f})")


if __name__ == "__main__":
    main()