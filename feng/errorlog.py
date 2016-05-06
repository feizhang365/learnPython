__author__ = 'fzh'

import logging
#logging level setting
logging.basicConfig(level=logging.INFO)
def fn(s):
    n = int(s)
    logging.info('n = %d' % n)
    print 10/n

fn('2')


