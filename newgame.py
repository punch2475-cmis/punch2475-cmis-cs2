import random

def guess1(tries=5, number=0):
    if tries == 5:
        number = random.randint(0,100)
        raw_input("Let's start you have 5 tries:")
    if tries == 0:
        print "You Suck"
        return False
    else:
        target = float(raw_input("Guess a number: "))
        if target == number:
            print "Correct!"
            return True
        elif target < number:
            print "Too low"
            return guess1(tries-1, number)
        else:
            print "Too high"
            return guess1(tries-1, number)

def guess2(tries=5,target=0):
    if tries == 5:
        print "5 tries to go!"
    if tries == 0:
        print "Computer, you suck at this"
        return False
    else:
        if tries == 1:
            target = random.randint(0, 100)
        else:
            target = random.randint(0,100)
        result = raw_input(("Computer's guess: {} (c, l, or h)".format(target)))
        if result == "c":
            print "Correct"
            return True
        elif result == "l":
            print "Too low"
            return guess2(tries-1,target)
        else:
            print "Too high"
            return guess2(tries-1,target)

            
def rounds(number_rounds, guess1_score, guess2_score):
    if number_rounds == 0:
        if guess1_score > guess2_score:
            winner = "You"
        elif guess1_score < guess2_score:
            winner = "Computer"
        elif guess1_score == guess2_score:
            winner = "No one"
        print "{} wins!".format(winner)
    else:
        if guess1()==True:
            guess1_score += 1
        if guess2() == True:
            guess2_score += 1
        return rounds(number_rounds - 1, guess1_score, guess2_score)

def main():
    number_rounds=3
    guess1_score =0
    guess2_score =0
    rounds(number_rounds,guess1_score,guess2_score)

main()



