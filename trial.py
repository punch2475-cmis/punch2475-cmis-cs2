def add(x,y):
	z=x+y
	return z

def output(name,grade,x,y,z):
	return """
Hello, My name is {}.
I'm in {} grade.
I will show you how to add.
{}+{}={}
""". format(name,grade,x,y,z)

def main():
	name=raw_input("What is your name?:")
	grade=raw_input("What grade are you?:")
	x=raw_input("type radom interger:")
	y=raw_input("type another:")
	z=add(int(x),int(y))
	print output(name,grade,x,y,z)

main()
