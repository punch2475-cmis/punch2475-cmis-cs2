#Future major and GPA
def calA(a,b,c,d,e):
    return a+b+c+d+e

def main():
    name= raw_input ("What is your name?")
    age= raw_input("How old are you?")
    grade= raw_input ("Grade:")
    subjectA= subject()
    print subjecta
    study= studyyears()
    print study
    read= reading()
    print read
    gradeA= schoolgrade()
    print gradeA
    hw= homework()
    print hw
    personality= character()
    print personality
    sum1= calA(subjectA,study,read,gradeA,hw,personality)
    
    
def GPAa():
    if sum1 >= 6 <=0:
        print "2.0"
    if sum1 >= 7 <= 12:
        print "2.4 - 2.9"
    if sum1>= 13 <= 19:
        print "3.0-3.4"
    if sum1 >= 20 <= 25:
        print "3.5-4.0"
    return GPAa

def randomGPA():
    rdGPA = random.randint(2.0,4.0)
    rGPA = float(rdGPA+ GPAa)/2


def subject():
    subject= raw_input("""
What subject do you like?
a. math
b. science
c. art
d. computer science
e. english
f. economic 
(type a,b,c,d,e,f):
               """)
    if subject== "a":
        return 1
    if subject== "b":
        return 2
    if subject== "c":
        return 3
    if subject== "d":
        return 4
    if subject== "e":
        return 5
    if subject== "f":
        return 6

def studyyears():
    studyyears= raw_input ("""
How many years you want to study?
a. less than 3
b. 3
c. 4
d. 5
e. 6
(type a,b,c,d,e):
               """)
    if studyyears== "a":
        return 1
    if studyyears== "b":
        return 2
    if studyyears== "c":
        return 3
    if studyyears== "d":
        return 4
    if studyyears== "e":
        return 5

def reading():
    reading= raw_input("""
How do you feel about reading?
a. I hate it
b. It's okay
c. I love it
(type a,b,c):
            """)
    if reading== "a":
        return 1
    if reading== "b":
        return 2
    if reading== "c":
        return 3

def schoolgrade():
    schoolgrade= raw_input("""
What is your current grade?
a. F
b. D
c. C
e. A-B
(type a,b,c,e):
            """)
    if schoolgrade == "a":
        return 1
    if schoolgrade == "b":
        return 2
    if schoolgrade == "c":
        return 3
    if schoolgrade == "e":
        return 4

def homework():
    homework=raw_input("""
How often did you finish homework?
a. Never
b. Rarely
c. Always
(type a,b,c):
            """)
    if homework == "a":
        return 1
    if homework == "b": 
        return 2
    if homework == "c":
        return 3

def character():
    character=raw_input("""
Which of these character best suit for you?
a. I'm not organized
b. I'm very organized
(type a,b):
        """)
    if character == "a":
        return 1
    if character == "b":
        return 2
def job ():
    if sumOfeverthing >= 10:
        print "you can study in major __________"
    if sumOfeverything >= 11 <= 19:
        print "you can study in major __________"
    if sumOfeverything >= 20 <= 24:
        print "you can study in major __________"

def output():
	output="""
Hello {}, you are {} years old. You are in grade {}. 
From the quiz that you take, your future job is going to be {}. Also you will graduate with GPA {}. 
""". format(name,age,grade)
    if sum1 >=6:
        print """
Hello {}, you are {} years old.
You are in grade {}.
From the quiz you take above, your future job will be in {}. 
Also you will graduate with GPA {}. 
""". format(_jsgjlks;lgj.__gklsjgl.__.)

main ()

    
