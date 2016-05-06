# -*- encoding:utf-8 -*- #
__author__ = 'fzh'

s = r'ABC\-001' # Python的字符串
print s

import re
print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print 'ok'
else:
    print 'failed'


print 'a b   c'.split(' ')
print re.split(r'\s+', 'a b   c')

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group(0)
print m.group(1)
print m.group(2)
