__author__ = 'fzh'
import time
import calendar
ticks = time.time()
print ticks
localtime = time.localtime(time.time())
print "Local current time :", localtime

cal = calendar.month(2015,6)
print cal

def printme( str ):
   "This prints a passed string into this function"
   print str
   return

printme("test function")


