__author__ = 'fzh'
# Fibonacci numbers module
''' Fibonacci numbers module'''

def fib(n):
    a,b = 0,1
    while b < n :
        print b,
        a,b = b,a+b

# fib(10)

print "\n==============="

def fib2(n):# return Fibonacci series up to n
    result = []
    a,b = 0,1
    while b < n :
        result.append(b)
        a,b = b,a+b
    return result# return Fibonacci series up to n

# print fib2(100)