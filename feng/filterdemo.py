__author__ = 'fzh'

def is_odd(x):
    return x%2 == 1

print filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15])

def  not_empty(s):
    return s and s.strip()

print filter(not_empty,['A', '', 'B', None, 'C', '  '])