__author__ = 'fzh'

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_score(self):
        print '%s : %s' %(self.name,self.age)

tom = Student('Tom',28)
figo = Student('Figo',33)

tom.print_score()
figo.print_score()
