__author__ = 'fzh'
# def print_func(par):
#     print "Hello : ", par
#     return
import support
import math
support.print_func("feizhang")

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1
   print Money
   return
AddMoney()
print Money

content = dir(math)
print content