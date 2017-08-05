# -*- encoding: utf-8 -*- #
__author__ = 'fzh'
import numpy as np

a = np.array([1, 2, 3, 4])

c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
# shape of the array
print(c.shape)
# change the shape of array
# c.shape = 4,3
print(c)
# reshape array
d = a.reshape((2,2))
print "reshape string is "
print(d)
a[1] = 100
print a
print d

#arange step
ss = np.arange(0,10,1)
print ss

#linespace
ls = np.linspace(1,2,5)
print ls