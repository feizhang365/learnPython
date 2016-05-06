__author__ = 'fzh'

import os

print os.name
print os.uname()
print os.environ
print os.getcwd()
print os.getenv('path')

print [x for x in os.listdir('.') if os.path.isdir(x)]

# serialization
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='bob',age =20 ,score = 88)
pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d,f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d


#JSON

import json
d = dict(name='feizhang',age=32,score=100)
print json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print json.loads(json_str)
