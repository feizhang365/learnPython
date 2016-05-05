__author__ = 'fzh'
def add_end(L=[]):
    L.append('END')
    return L

f0  = add_end()
print f0
f = add_end([1,2,3])
print f
f1  = add_end(['x', 'y', 'z'])
print f1

add_end()
add_end()
print add_end()

def add_end2(L=None):
    if L is None:
        L = []
    L.append("end")
    return L

add_end2()
print(add_end2())