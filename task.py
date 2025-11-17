# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
# Try to expand your implementation as best as you can.
# Think of as many features as you can, and try implementing them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
#
# When you are done upload this code to your github repository.
#
# Delete these comments before commit!
# Good luck.


class Student:
    def __init__(self, name):
        self.name = name


class Highschool:
    def __init__(self, student):
        # self.math = math
        # self.chemistry = chemistry
        self.students_list = []
        self.student = student

    # def math(self, grade, math_attendence):
    #   self.students_grades = []
    #  self.students_attendence = []

    def add_student(self, Student):
        self.students_list.append(self.student)

    def student_list(self, students_list):
        return self.students_list


Student1 = Student(name="Sebastian")
Student2 = Student(name="Jan")
highschool1 = Highschool(Student1)
highschool1.add_student(Student2)
print(highschool1.students_list)
