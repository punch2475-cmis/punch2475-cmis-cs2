import math
def add(a,b):
	return a+b

print add(3,4)

def sub(a,b):
	return a-b

print sub(5,3)

def mul(a,b):
	return a*b

print mul(4,4)

def div(a,b):
	return a/b

print div(2,3.0)

def divhrs(a,b):
	return a/b

print divhrs(86400,3600)

def area(a):
	return math.pi* a **2

print area(5)

def volume(a):
	return ((4/3.0)*math.pi)*a**3)

print volume(5)

def avgvol(a,b): 
	return (volume(a)+volume(b))/2

print avgvol(5.0,10.0)

def areatri(a,b,c):
	s=(a+b+c)/2
	s1
	
def msg_box(word):
	return "+"+((len(word)+ 4)*"-") +"+"+ "\n" + "|" + (2*" ") + (word) +(2* " ")+ "|" + "\n" + "+" + ((len(word))+ 4)*"-") +"+"+ "\n" + "|" + (2*" ")
	
print msg_box("Hello")
print msg_box("I eat cats!")
	


