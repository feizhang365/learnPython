__author__ = 'fzh'
# write to text file
textFile = open("out.txt","w")
for i in [1,2,3,4,5,6,7,8,9,100]:
    textFile.write("\n number"+str(i))
