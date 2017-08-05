# -*- encoding: utf-8 -*- #
__author__ = 'fzh'
import os;

f = open("__init__.py","r")
for line in f:
    print line
f.close()

a = os.path.abspath("")
print(a)