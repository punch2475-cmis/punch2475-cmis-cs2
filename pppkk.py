#this text game will help you determine which phone is best for you by answering 3 questions. So from this the program will use the input to calculate the phone that is best for he/she. 


import random

def main():
	Name= raw_input("Your name:")
	phone= raw_input("Your current phone:")
	afford= money()
	use= rely()
	password= security()
	superRandom= random1()
	sp= smartphone()
	calA= cal(afford,use,superRandom,password,randomA)

def cal(afford,use,superRandom,password,randomA):
    return  afford+use+superRandom+password+randomA

    
def smartphone():
	calA= cal(afford,use,superRandom,password,randomA)
	if calA <=3:
		return "Nokia 3310"
	if calA <=6:
		return " Iphone6s"
	if calA <= 8:
		return " Samsung s7"
	if calA <= 9:
		return " Samsung a7"
	if calA >= 10:
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
    if rely== "b":
        return 2
    if rely== "c":
        return 3
    if rely== "d":
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
    if money== "a":
        return 1
    if money== "b":
        return 2
    if money== "c":
        return 3
    if money == "d":
        return 4
    else:
        random.randint(1,4)

def random1():
	random1= raw_input("""
How do you want to calculate your result?
a. use random to select your phone
b. I don't care
c. don't use random
d. Whatever
(type a,b,c,d):
		""")
	if random1== "a":
		return random.random()/20
	if random1 == "b":
		return random.randint(1,90)/7
	if random1== "c":
		return 3
	if random1== "d":
		return random.random()
	else:
		return random.randint(1,4)

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
	if security == "b":
		return 2
	if security == "c":
		return 0
	if security == "d":
		return 3
	else:
		return random.random()


	
def output(Name,phone,sp):
	out = """
Hello {}, 
You are currently using {}.
This program will help you to decide to buy a phone that best suit for you.
From the test that you take
The result is {}. 
""". format(Name,phone,sp)
	return out

main()

