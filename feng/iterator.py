__author__ = 'fzh'
# -*- coding:utf-8 -*-
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print key


print "-------------"

for v in d.itervalues() :
    print v


# string

for ch in "ABC":
    print ch

print isinstance('abc', Iterable) # str是否可迭代

print isinstance([1,2,3], Iterable) # list是否可迭代

print isinstance(123, Iterable) # 整数是否可迭代


for k,v in enumerate(["A","B","C"]):
    print k,v