__author__ = 'fzh'
'''
5.1.2. Using Lists as Queues
'''

from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()

print(queue)