# -*- encoding: utf-8 -*- #
__author__ = 'fzh'
#filter demo

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
res1 = filter(lambda x: x % 2, fib)
print res1

res2 = filter(lambda x: x % 2 == 0, fib)
print res2