
def oddeven():
    for count in range(1,2001):
        print "number is " + str(count) + "."
        if count%2 == 0:
            print "This is an even number."
        else:
            print "This is an odd number."


oddeven()