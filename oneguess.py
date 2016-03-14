import random
import math

def dif(targetNumber, rd):
    return abs(targetNumber-rd) 

def output(): 
    out="""
What is the minimum number? {}
What is the maximum number? {}
I thinking of a number from {} to {}
What do you think it is? {}

The target was {}
Your guess was {}
""". format(mininumber,maxnumber,mininumber,maxnumber,rd,targetNumber,rd)

def main():
	mininumber= raw_input("What is the minimum number?")
    maxnumber= raw_input ("What is the maximum number?")
    rd= raw_input ("What do you think it is?")

    targetNumber= random.randint(mininumber,maxnumber)
    if targetNumber = rd 
        print ":)"
    else 
        print dif

main()


    
