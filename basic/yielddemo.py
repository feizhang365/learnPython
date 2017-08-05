# -*- encoding: utf-8 -*- #
__author__ = 'fzh'


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        # yield b
        print b
        a, b = b, a + b
        n = n + 1
        print n,a,b

f = fab(5)
f.next()