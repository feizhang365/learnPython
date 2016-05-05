__author__ = 'fzh'
# default argument value
def f(a,L=[]):
    L.append(a)
    return L
print f(1)
print f(2)
print f(3)