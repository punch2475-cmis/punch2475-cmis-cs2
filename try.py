
while False:
	print ":("

#x=10
#while x >=0:
#	print x
#	x -=1 
def countdown(x):
	while x >=0:
		print x
		x-=1

def countup(x):
	while x<10:
		print x
		x+=1
def count(x):
	while x < 0:
		print x
		x+=1
	while x >0:
		print x
		x-=1
def countFrom2(x,y):
	print x
	while x > y:
		print x-1
		x-=1
	while x < y:
		print x+1
		x+=1
def addOdd(n):
	sum = 0
	if n >0:
		while n > 0:
			if n % 2 ==1:
				sum+= n
			n-=1
	elif n <0:
		while n > 0:
			if n % 2 ==1:
				sum+= n
			n+=1
	return sum

def grid(w,h):
	out =""
	x = 0
	while x < w:
		out += "."
		x+=1
	while x < h:
		out += "."
		x+=1
	return out
	
print grid (10,5)
	



