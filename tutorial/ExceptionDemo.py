__author__ = 'fzh'

while True:
    try:
        x = int(raw_input("Please input a number "))
        break
    except ValueError:
        print "Oops! this is not a valid Number. Try Again.."
