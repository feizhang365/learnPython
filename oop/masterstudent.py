# -*- encoding: utf-8 -*- #
__author__ = 'fzh'
from student import Student
# object inherited
class MasterStudent(Student):
    internship = "ffffff"

james = MasterStudent('james')
print james.internship
james.set_age(30)
print james.age