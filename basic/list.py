__author__ = 'fzh'
'''This is comment of the code
   Good comment is part of good code '''
#list test
listA = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
s = ['python', 'java', ['asp', 'php'], 'scheme']
print listA          # Prints complete list
print listA[0]       # Prints first element of the list
print listA[1:3]     # Prints elements starting from 2nd till 3rd
print listA[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print listA + tinylist # Prints concatenated lists

print listA.pop(2)
print listA
''' isinstance  '''
print "is snstance of ::",isinstance(tinylist,list)