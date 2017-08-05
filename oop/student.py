# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

# create a Student class
class Student(object):
    def __init__(self,name):
        self.name = name
    def set_age(self,age):
        self.age = age
    def set_major(self,major):
        self.major = major

fei = Student('fei')
fei.set_age(31)
fei.set_major('computer science')


