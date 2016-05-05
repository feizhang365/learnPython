__author__ = 'fzh'

#map
def f(x):
    return x * x
res = map(f,[1,2,3,5,7])
print res

print  map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

#reduce
def add(x,y):
    return x + y
print reduce(add,[1,3,5,7,9])

def fn(x,y):
    return x*10 +y
print reduce(fn ,[1,3,5,7,9])