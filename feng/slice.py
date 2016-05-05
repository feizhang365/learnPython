__author__ = 'fzh'

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

r = []
n = 3
for i in range(n):
    r.append(L[i])

print r

print L[0:3]
print L[:3]

L2 = range(100)
print L2
print L2[0:10]
print L2[:20:2]