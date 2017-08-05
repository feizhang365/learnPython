# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

res = reduce(lambda x,y: x+y, [47,11,42,13])
print res

#Determining the maximum of a list of numerical values by using reduce:
f = lambda a,b: a if (a > b) else b
res2 = reduce(f, [47,11,42,102,13])
print res2

#Calculating the sum of the numbers from 1 to 100:
res3 = reduce(lambda x, y: x+y, range(1,101))
print res3