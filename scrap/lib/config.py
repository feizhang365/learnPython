# -*- coding: utf-8 -*-

import os


def load(name):
    dir_cfg = os.getenv('SYS_ROOT')
    fn = os.path.join(dir_cfg,'etc',name)
    text = file(fn).read()
    s = eval(text)
    return s
        
def loadcfg(name):
    text = file(name).read()
    print text
    s = eval(text)
    return s

if __name__ == '__main__':
    cfg = load('test.conf')
    print cfg['AUTHOR']