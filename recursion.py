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
        
def adder():
    n= raw_input("Next Number:")
    if n =:
        print "The total:"
    else:
        adder()

    
    
    

def main():
    adder()
    return

main()
	
