# QUESTION 1:

"""
Implement the following class:

Student
name: string
id: string
grade: Dict[int, float] (A dictionary where the key is an integer representing the course ID, and the value is a float representing the grade.)
is_active: boolean
Methods:
__init__(name: string, id: string): Constructor
add_grade(course_id: int, grade: float) -> void: Adds a grade to the student
get_average_grade() -> float: Returns the average grade
toggle_active_status() -> void: Toggles the active status
After implementing the class, apply the Prototype Design Pattern to allow deep cloning of the instance. Then:

Create a student instance with data of your choice.
Clone it.
Add a grade to the cloned student and verify that the original student does not have this new grade.
----------------------------------------------------------------------------------------------------
"""

import copy
from abc import ABC, abstractmethod
from typing import Dict


# Prototype Interface
class Student(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete Student Class
class ConcreteStudent(Student):
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        self.grades: Dict[int, float] = {}
        self.is_active = True

    def add_grade(self, course_id: int, grade: float) -> None:
        self.grades[course_id] = grade

    def get_average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def toggle_active_status(self) -> None:
        self.is_active = not self.is_active

    def clone(self):
        return copy.deepcopy(self)


# Create a student instance
student1 = ConcreteStudent("Wisam Gibran", "S1234567")
student1.add_grade(101, 88.5)
student1.add_grade(102, 92.0)

# Clone the student instance
student2 = student1.clone()

# Add a new grade to the cloned student
student2.add_grade(103, 95.0)

# Verify that the original student remains unchanged
print("Original Student Grades:", student1.grades)
print("Cloned Student Grades:", student2.grades)
