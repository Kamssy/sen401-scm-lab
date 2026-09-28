"""Main script: runs a demo of the student records application."""

from students import students, add_student, average_score
from utils.helpers import highest_score, lowest_score


def main():
    print("=== Student Records Demo ===")
    add_student("Ngozi", 74)

    print("\nCurrent students:")
    for s in students:
        print(f"  {s['name']}: {s['score']}")

    print(f"\nAverage score: {average_score(students):.2f}")
    top = highest_score(students)
    bottom = lowest_score(students)
    print(f"Highest: {top['name']} ({top['score']})")
    print(f"Lowest:  {bottom['name']} ({bottom['score']})")


if __name__ == "__main__":
    main()