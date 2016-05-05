__author__ = 'fzh'
#List
L = [x * x for x in range(10)]
print L
#generator
g = (x * x for x in range(10))
print g.next()
print g.next()
print g.next()

for n in g:
    print n