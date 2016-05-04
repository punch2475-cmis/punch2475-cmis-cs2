import random 

def guess():
	n= raw_input("Number:")
	target= random.randint(1,100)
	
	print target

	if n == target:
		print "good"
	if n < target:
		print "too low"
	if n > target:
		print "too high"
guess()
