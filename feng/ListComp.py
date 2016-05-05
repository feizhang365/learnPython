# -*- coding:utf-8 -*-
__author__ = 'fzh'

#list
print range(1,11)

# another list
L = []
for x in range(1,11):
    L.append(x * x)
print L

# one line code
print [ x * x for x in range(1,11)]

print [ x * x for x in range(1,11) if x % 2 ==0]

print [ x + y for x in 'ABC' for y in '123']


print [ x + y for x in 'ABCDEFGHIJKLMN' for y in '123456789']

import os
print [d for d in os.listdir(".")] # os.listdir可以列出文件和目录


d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.iteritems():
    print k,v

# to lower case
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s,str)]
