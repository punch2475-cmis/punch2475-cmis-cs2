#Section 1: Terminology
# 1) What is a recursive function?
# A recursive function is a function that call itself 
#
# 2) What happens if there is no base case defined in a recursive function?
# Without the base the recursive function wouldn't be complete and it will get an error message. 
#
#
# 3) What is the first thing to consider when designing a recursive function?
#The first thing to consider when designing a recusive function is the base case which is 
#
#
# 4) How do we put data into a function call? x
#
#put it to variable for example p= output()
# 
# 5) How do we get data out of a function call? 
#
# return or print
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2
#b3 = 4

#c1 = -2
#c2 =  4
#c3 =  45

#d1 = 6
#d2 = 8
#d3 = 2 x

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

#Grading:
# +2 base case is present (MUST BE LABELED)
# +2 recursive case is present (MUST BE LABELED)
# -1 base case returns sum/ct (or equivalent)
# -2 recursive case filters even numbers
# -1 recursive case increments sum and ct correctly
# -1 recursive case returns correct recursive call
# +1 main function present AND called  

def type1():
    n= raw_input("Next: ")
    if n == "":
        return avgodd #base case
    else: 
        return type1() #recursive case

def odd(n):
    if n/2 == int:
        return 0
    else: 
        return n

#def avgOfodd():

def main():
    t= type1()
    odd1= odd(n)

main()
def output():
    """ The average of odd number is{}""". format(avgOfodd)
    
 

