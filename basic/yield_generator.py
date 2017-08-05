# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print i


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
for i in mygenerator:
    print i