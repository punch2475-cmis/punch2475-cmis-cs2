#this text game will help you determine which phone is best for you by answering 3 questions. So from this the program will use the input to calculate the phone that is best for he/she. 
import random

def main():
	Name= raw_input("Your name:")
	phone= raw_input ("Your current phone:")
	sp= smartphone()
	cp= currentPhone()
	p=output(Name,phone,cp,sp)
	print p


def calculation(afford,use,superRandom,password):
    return  afford,use,superRandom,password

    
def smartphone():
	afford= money()
	use= rely()
	superRandom= random1()
	password= security()
	phoneModel = calculation(afford,use,superRandom,password)
	if phoneModel <=3:
		return "Nokia 3310"
	if phoneModel <=5:
		return " Iphone6s"
	if phoneModel <= 8:
		return " Samsung s7"
	if phoneModel <= 10:
		return " Samsung a7"
	if phoneModel < 11:
		return " Samsung Note5"
	if phoneModel > 12:
		return "Samsung Note4"

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
    if money== "a" and "b" and "c" and "d":
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
	if not security == "a" or security == "d":
		return 0
	elif security == "a" and "d":
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

def currentPhone():
	currentPhone=raw_input("""
Do you think your phone suit you?
(type y or n):
		""")
	if currentPhone == "y":
		return True
	else:
		return False

def output(Name,phone,cp,sp):
	out = """
Hello {}, 
You are currently using {}.
This program will help you to decide to buy a phone that best suits you.
I think my current phone suit me: {}
From the test that you took
The result is {}. 
""". format(Name,phone,cp,sp)
	return out

main()

