from main import StudentsInMLOps
import pytest

@pytest.fixture
def students():
    return StudentsInMLOps()

def test_enroll_students(students):
    students.enrollStudents(5)
    assert students.getTotalStrength() == 5

def test_drop_students(students):
    students.enrollStudents(10)
    students.dropStudents(3)
    assert students.getTotalStrength() == 7

def test_class_name(students):
    assert students.getClassName() == "MLOps"
