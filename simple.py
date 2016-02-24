import math
#pythagorean theorem 
#a**2+b**2=c**2

def  cal(legA, legB):
	return math.sqrt((legA)**2+(legB)**2)


def output(legA,legB,legC):
  out = """
Solve triangle
Shortest length of your triangle is{}
Second longest length of your triangle is {}
So your hypotenuse is {}
""". format(legA,legB,legC)
  return out

def main():
  legA=raw_input("shortest length:")
  legB= raw_input("second longest length:")
  legC= cal(float(legA),float(legB))
	

  p=output(legA,legB,legC)
  print p 

main()






