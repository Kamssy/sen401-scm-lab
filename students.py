from pydantic import BaseModel, Field

MIN_SCORE = 0
MAX_SCORE = 100

class Student(BaseModel):
    """A single student record with validated fields."""

    name: str = Field(min_length=1)
    score: float = Field(ge=MIN_SCORE, le=MAX_SCORE)

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