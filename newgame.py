import random

def guess1(tries, target):
    if tries == 5:
        target = random.randint(0,100)
    if tries == 0:
        print "You suck at this"
        return False
    else:
        guess = float(raw_input("Guess a number: "))
        if guess == target:
            print "Correct!"
        elif guess < target:
            print "Too low"
            return guess1(tries-1, target)
        else:
            print "Too high"
            return guess1(tries-1, target)
def guess2(tries):
        random3= random.randint(0,100)
        if tries >=1:
                print "I guess {}." .format(random3)
                result= raw_input("(H)igh, (L)ow, (C)orrect")
                if result == "C":
                    print "Awesome"
                elif result == "H":
                    print "Too high"
                    return guess2(tries -1)
                else:
                    print "Too low"
                    return guess2(tries -1)
                if tries == 0:
                    print "T_T"
                else: 
                    guess2(tries-1)
            
def rounds(number_rounds,tries,target):
    if number_rounds == 0:
        print "Done"
    else:
        number_rounds = 2
        print "You have", (number_rounds-1),"round left"
        return guess1(tries-1, target) 

def main():
    tries= 5
    target=0
    number_rounds=3
    guess1(tries,target)
    guess2(tries)
    rounds(number_rounds,tries,target)

main()



