#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 398 < 100*40+5
#b) 5 > 3*2-5
#c) 76 >= 3*4*4
#
#2) What does 'return' do?
# The keyword "return" the job is to spitting the value.
#
#
#3) What are 2 ways indentation is important in python code?
#a) Indentation tells where the function definition begins and ends.
#b) Indentation also tells the function what to spit value, if the statement is true.
#
#

#PART 2: Reading
#Type the values for 9 of the 12 of the variables below.
#
#problem1_a) 36
#problem1_b) -square root 3
#problem1_c) 0
#problem1_d) -5
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) False
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a)  7
#problem4_b)  5
#problem4_c)  0.125
#problem4_d)  5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def trueexpression(a,b,c): #check the greatest number
    if a > b and a > c: 
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else: 
        return false
        
def main():
    print "Type in 3 different numbers (decimals are Ok!)" 
    a= float(raw_input("A:"))
    b= float(raw_input ("B:"))
    c= float(raw_input ("C:"))
    
    statement = trueexpression(a,b,c)
    
    print output(statement)

def output(statement):
  if statement == False:
      return "You didn't follow instructions"
  else:
      return "The largest number is {}". format(statement)
     

main()
