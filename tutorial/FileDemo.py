__author__ = 'fzh'

# f = open("test.txt","r")
# print 'begin read line'

with open("test.txt","r") as f:
    for line in f:
        print line