# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

'''
关键字参数
'''

def add(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum +=v
    return sum

dict = {'x': 2, 'y': 6}
sumValue = add(**dict)
print sumValue