__author__ = 'fzh'
#triditional
def calc_sum(*args):
    ax = 0
    for i in args:
        ax = ax + i
    return ax

print calc_sum(1,2,3,5,7)

# return func
def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum

f = lazy_sum(1,2,3,5,7)
print f()


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1()


#anymouse func
f = lambda x: x * x
print f(2)

def build(x, y):
    return lambda: x * x + y * y

rs = build(3,4)
print rs()

def int2(x, base=2):
    return int(x, base)
print int2("100")