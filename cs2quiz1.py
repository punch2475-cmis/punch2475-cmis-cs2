#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# = is call assignment operator which use to put variable to value.
#
#
#2 3pts) Write a technical definition for 'function'
#
#Function is name sequence of statement that perform a computation.
#
#3 1pt) What does the keyword "return" do?
#
# The keyword "return" the job is to spitting the value.
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: boolean bool("Punch"), bool(45678)
#	2: interger int(787),int(6768)
#	3: float float(8.8),float(6697.09)
#	4: string str(Punch), str(ajkfj)
#	5: tuple
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#Fuction definition is process of defining function and make the function availble to the program. Function call is language statement that request the fuction.
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Input:insert the value
#	2: Processing: the computer perform calculation
#	3: Output: give output or result and end the process
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi


import math
def diameter(x):
    return 2*(math.sqrt(x/math.pi))
def total_diameter(d1,d2,d3):
    return d1+d2+d3

def output(d1,d2,d3,total):
    out="""
Circle      Diameter
c1             {}
c2             {}
c3             {}
Totals:        {}
""".format(d1,d2,d3,total)
    return out

def main():
    C1=raw_input("Area of Circle1: ")
    C2=raw_input("Area of Circle2: ")
    C3=raw_input("Area of Circle3: ")
    
    d1=diameter(float(C1))
    d2=diameter(float(C2))
    d3=diameter(float(C3))
    total=total_diameter(d1,d2,d3)
    
    out=output(d1,d2,d3,total)
    print out

main()

    

