import math
#pythagorean theorem 
#a**2+b**2=c**2

def  cal(legA, legB):
	return math.sqrt((legA)**2+(legB)**2)


def output(Name,legA,legB,legC):
	out = """
Hello {}, This program will help you solve triangle by using pythagorean theorem.
Shortest length of your triangle is{}
Second longest length of your triangle is {}
So your hypotenuse is {}
""". format(Name,legA,legB,legC)
	return out

def main():
	Name= raw_input("What is your name?:")
	legA=raw_input("shortest length:")
	legB= raw_input("second longest length:")
	legC= cal(float(legA),float(legB))
	
	p=output(Name,legA,legB,legC)
	print p 

main()






