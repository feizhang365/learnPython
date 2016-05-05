__author__ = 'fzh'

'''
Functional Programming Tools
'''

def f(x): return x % 3 == 0 or x % 5 == 0

rr = filter(f,range(2,25))

print(rr)

print "------------------------"

def cube(x): return x*x*x

mp = map(cube ,range(1,11))

print mp

print "------------------------"

seq = range(8)
def add(x,y):return x+y

mp2 = map(add,seq,seq)

print mp2

print "--------------------------"