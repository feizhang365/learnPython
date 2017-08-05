# -*- encoding: utf-8 -*- #
__author__ = 'fzh'
# Map demo
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
res2 = map(lambda a,b:a+b,a,b)
print res2

res3 = map(lambda a,b,c:a+b+c,a,b,c)
print res3