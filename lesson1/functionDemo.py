__author__ = 'fzh'
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return


list2 = [10,20,30]
changeme(list2)


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist

# Function definition is here
# def printme( str ):
#    "This prints a passed string into this function"
#    print str;
#    return;

# Now you can call printme function
#printme();

def printme( str ):
   "This prints a passed string into this function"
   print str;
   return;

# Now you can call printme function
printme( str = "My string");

#The following example gives more clear picture. Note that the order of parameters does not matter
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name;
   print "Age ", age;
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" );


#default arg# Function definition is here
def printinfoDefault( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name;
   print "Age ", age;
   return;

# Now you can call printinfo function
printinfoDefault( age=50, name="miki" );
printinfoDefault( name="miki" );


#Variable-length arguments
# Function definition is here
def printinfoVar(*vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   # print arg1
   for var in vartuple:
      print var
   return;

# Now you can call printinfo function
# printinfoVar( 10 );
# printinfoVar( 70, 60, 50 );
printinfoVar();


