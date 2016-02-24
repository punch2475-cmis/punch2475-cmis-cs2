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

def volume(radius):
	return 1.33333333333 * math.pi * (radius**3) #
print volume(5)

def avg_volume (diameter1, diameter2):
    vsphere1=volume(diameter1/2)
    vsphere2=volume(diameter2/2)
    return (vsphere1+vsphere2)/2
print avg_volume(10, 20)

def area2 (a, b, c):
	return math.sqrt (2.75*(2.75-a)*(2.75-b)*(2.75-c))
	
print area2 (1.0, 2.0, 2.5)
    
def right_align(word):
	return str ((80-len(word))*" " + word)
	
print right_align("Hello")

def center(term):
	return str ((40-len(term))*" " + term) 
	
print center ("Hello")
	
def msg_box(word):
	return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word)+ 4)*"-") + "+" #message box
	
print msg_box("Hello")
print msg_box("I eat cats!")
	
a=add(3,4)
b=sub(5,3)
c=mul(4,4)
d=div(2,3.0)
e=divhrs(86400,3600)
f=area(5)
g=volume(5)
h=avg_volume(10, 20)
i=area2(1.0, 2.0, 2.5)
j=right_align("Hello")
k=center ("Hello")
l=msg_box("Hello")
m=msg_box("I eat cats!")

ab=add(3,4)
cd=sub(5,3)
ef=mul(4,4)
gh=div(2,3.0)
ij=divhrs(86400,3600)
kl=area(5)
mn=volume(5)
op=avg_volume(10, 20)
qr=area2(1.0, 2.0, 2.5)
p=right_align("Hello")
z=center ("Hello")
x=msg_box("Hello")
y=msg_box("I eat cats!")

print msg_box(str(a))
print msg_box(str(b))
print msg_box(str(c))
print msg_box(str(d))
print msg_box(str(e))
print msg_box(str(f))
print msg_box(str(g))
print msg_box(str(h))
print msg_box(str(i))
print msg_box(j)
print msg_box(k)
print l
print m
print msg_box(str(ab))
print msg_box(str(cd))
print msg_box(str(ef))
print msg_box(str(gh))
print msg_box(str(ij))
print msg_box(str(kl))
print msg_box(str(mn))
print msg_box(str(op))
print msg_box(str(qr))
print msg_box(p)
print msg_box(z)
print x
print y



