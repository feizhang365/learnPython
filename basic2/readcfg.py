__author__ = 'fzh'
# read config file properties
import os
def load(name):
    text = file(name).read()
    print text
    s = eval(text)
    return s

if __name__ == '__main__':
    print "==========="
    cfg = load('test.conf')
    print cfg['AUTHOR']