import random

def main():
    mininumber= int(raw_input("What is the minimum number?"))
    maxnumber= int(raw_input ("What is the maximum number?"))
    print "I am thinking of a number between", mininumber, "and", maxnumber, "." 
    guess = int(raw_input("What do you think it is ?"))
    number_range = random.randint(mininumber, maxnumber)
    difference = abs(guess-number_range)
    out= output(number_range,guess,difference)

def output(number_range,guess,difference): 
    if guess == number_range:
        print """
The target was {}.
Your guess was {}.
That is correct! You must be a phychic!
""". format(number_range,guess)

    elif guess > number_range:
        print """
The target was {}.
Your guess was {}.
That's over by {}.
""". format(number_range,guess, difference)

    elif guess < number_range:
        print """
The target was {}.
Your guess was {}.
That's under by {}.
""". format(number_range,guess,difference) 

main()
