
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
	if n >0:
		while n%2== 1:
		sum+= n
		print n
	if n <0:
		while n% 2 ==0:
		return 0
 
def main():
	addOdd(3)

main()
