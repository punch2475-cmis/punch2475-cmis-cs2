#this text game will help you determine which phone is best for you by answering 3 questions. So from this the program will use the input to calculate the phone that is best for he/she. 
import random

def main():
	Name= raw_input("Your name:")
	phone= raw_input ("Your current phone:")
	sp= smartphone()
	b1=out()
	p=output(Name,phone,b1,sp)
	print p


def cal(a,b,c,d):
    return  a+b+c+d

    
def smartphone():
	afford= money()
	use= rely()
	superRandom= random1()
	password= security()
	calA= cal(afford,use,superRandom,password)
	if calA <=4:
		return "Nokia 3310"
	if calA <=6:
		return " Iphone6s"
	if calA <= 8:
		return " Samsung s7"
	if calA <= 9:
		return " Samsung a7"
	if calA > 10:
		return " Samsung Note5"
	if calA >= 1000:
		return "Use whatever you want"

def rely():
    rely= raw_input("""
What do typically rely on your smartphone?
a. playing games
b. calling people
c. for work
d. use for SNS(social network site)
(type a,b,c,d):
        """)
    if rely== "a":
        return 1
    elif rely== "b":
        return 2
    elif rely== "c":
        return 3
    elif rely== "d":
        return 4
    else:
        random.randint(1,4)

def money():
    money= raw_input("""
How much you can afford to spend on a smartphone?
a. 0.0 baht 
b. no worried my parent can afford for me
c. money is not my problem
d. I rather got it for free
(type a,b,c,d):
        """)
    if money== "a" or "b" or "c" or "d":
        return random.randint(1,3)
    else:
        random.randint(1,4)

def security():
	security= raw_input("""
What do you preferred for phone security
a. fingerprint
b. passwords
c. none, simple slider
d. a pattern
(type a,b,c,d):
	""")
	if security == "a":
		return 3
	elif security == "b":
		return 2
	elif security == "c":
		return 0
	elif security == "d":
		return 3
	else:
		return random.random()



def random1():
	random1= raw_input("""
How do you want to calculate your result?
a. use random to select your phone
b. I don't care
c. don't use random
d. Whatever
(type a,b,c,d):
		""")
	if random1== "a"or "b" or "c" or "d":
		return random.random()/2
	else:
		return random.randint(1,4)

def bool1():
	bool1=("""
Do you think your phone suit you?
(type y or n):
		""")
	if bool1 == "y":
		return True
	else:
		return False
def out():
	if bool1== True:
		return "I think my current phone suits me."
	else:
		return "I don't think my current phone suits me."

def output(Name,phone,b1,sp):
	out = """
Hello {}, 
You are currently using {}.
This program will help you to decide to buy a phone that best suits you.
{}
From the test that you took
The result is {}. 
""". format(Name,phone,b1,sp)
	return out

main()

