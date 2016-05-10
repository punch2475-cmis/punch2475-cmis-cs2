import random 

def guess():
	n= raw_input("Number:")
	target= random.randint(1,100)
	p= int(n)
	
	print target

	if p == target:
		print "good"
	if p < target :
		print "too low"
	if p > target:
		print "too high"
	guess()


guess()
