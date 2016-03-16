import random

def guess():
	import random
	minimum_num = int(raw_input("What is the minimum value?"))
	maximum_num = int(raw_input("What is the maximum value?"))
	rd = random.randint(minimum, maximum)
	print "I am thinking of a number between", minimum, "and", maximum
	guess = int(raw_input("What do you think it is?"))
	difference = abs(guess - rd)

	if guess == rd:
		print """
The target was {}
Your guess was {}
That is correct! You must be a phychic!
""".format(random, guessnumber)
	elif guess > rd:
		print """
The target was {}
Your guess was {}
That's over by {}
""".format(random, guessnumber, difference)
	elif guessnumber < random:
		print """
The target was {}
Your guess was {}
That's under by {}
""".format(random, guessnumber, difference)
	
guess()
