# -*- encoding:utf-8 -*- #
__author__ = 'fzh'

# namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print p.x
print p.y

# deque
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

# defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
dd['key1'] # key1存在
dd['key2'] # key2不存在，返回默认值