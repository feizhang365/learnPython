# -*- encoding: utf-8 -*- #
__author__ = 'fzh'
import os

with open("foo.txt") as f:
    for line in f:
        print(line)
    f.write()