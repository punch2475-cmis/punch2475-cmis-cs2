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
    print "Running Total:0"
    b= raw_input("Next Number:")

    

def main():
    adder()
    return

main()
	
