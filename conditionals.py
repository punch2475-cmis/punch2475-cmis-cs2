  #samsung or apple best suit for you
import random

def main():
    Name= raw_input("Your name:")
    Gender = raw_input ("Your gender")
    phone= raw_input ("Your current phone:")
	sp= smartphone()
   
	out= output
	print out


def cal(a,b,c):
    return  a+b+c



def output(name,gender,phone,smartphone2):
    output="""
Hello, {} 
Your gender is {}
Your current phone is{}
From the quiz that you take, the best smartphone brand that suit you is{}.
""". format(name,gender,phone,smartphone2)
    
def smartphone():
	afford= money()
	use= rely()
	superRandom= random1()
	calC= cal(afford,use,superRandom)
	if calC <=2:
		return "Nokia 3310"
	if calC <=4:
		return "Iphone6s"
	if calC <= 6:
		return "Samsung s7"
	if calC <= 8:
		return "Samsung a7"
	if calC >= 100:
		return "Samsung Note5"
	if calC >=1000:
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
d. Do want ever you want
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




main()

    
