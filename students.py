from pydantic import BaseModel, Field
class Student(BaseModel):
    """A single student record with validated fields."""

    name: str = Field(min_length=1)
    score: float = Field(ge=0, le=100)

students: list[Student] = [
    Student(name="Ada", score=91),
    Student(name="Tunde", score=58),
    Student(name="Chioma", score=76),
]
def add_student(name: str, score: float) -> Student:
    """Validate and add a new student. Raises ValidationError on bad input."""
    student = Student(name=name, score=score)
    students.append(student)
    return student

def average_score(data: list[Student]) -> float:
    """Return the average score, or 0 if the list is empty."""
    if not data:
        return 0
    return sum(s.score for s in data) / len(data)
