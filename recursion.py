def countup(n):
	if n>=10:
		print "Blastoff"
	else:
		print n
		countup(n+1)

def countdown(n):
    if n<= 0:
        print "Blastoff"
    else:
        print n
        countdown(n-1)

def countdown_from_to(start,stop):
    if start<stop:
        print "Blastoff"
    else:
        print start
        countdown_from_to(start-1,stop)

def countup_from_to(start,stop):
    if start>stop:
        print "Blastoff"
    else:
        print start
        countup_from_to(start+1,stop)
        
def adder(runningnumber):
    n= raw_input("Next Number:")
    if n != "":
        print "Running total: ", runningnumber + float(n)
        adder(runningnumber + float(n))
    else:
        print "The sum is",runningnumber



def biggest():
    a= raw_input("Next Number:")

    return biggest
    
    


    

def main():
    countup(56)
    adder(0)
    return

main()
	
