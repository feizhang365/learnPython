# -*- coding: utf-8 -*-
__author__ = 'fzh'

# 传统参数

def calc(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum

#调用的时候，需要先组装出一个list或tuple：
print calc([1,2,3])
print calc((1, 3, 5, 7))

#可变参数

def cald(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum

print cald(1,2)
print cald()

nums = [1, 2, 3]

print cald(*nums)


#关键字参数
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

print person("feizhang",32,male="M",married="yes")
kw = {'city': 'Beijing', 'job': 'Engineer'}

print person("feizhang",32,male="M",**kw)

print "==================="
#参数组合
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

print func(1, 2)
print func(1, 2, c=3)
print func(1, 2, 3, 'a', 'b')
print func(1, 2, 3, 'a', 'b', x=99)

args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)
