__author__ = 'fzh'
import os
print os.getcwd()
if os.path.exists('foo.txt'):
    data = open('foo.txt')
    for line in data:
        print line.split(" ")
    data.close()
else:
    print 'no data file foo.txt exist'

try:
    data = open('foo1.txt')
    for line in data:
        print line.split(" ")
    data.close()
except:
    print 'no data file foo.txt exist'