#Future 

def main():
    name= raw_input ("What is your name?")
    age= raw_input("How old are you?")
    grade= raw_input ("Grade:")
    
def subject():
    subject= ("""
What subject do you like?
a. math
b. science
c. art
d. computer science
e. english
f. economic 
(type a,b,c,d,e,f):
               """)
    if subject== "a" 
        return 1
    if subject== "b" 
        return 2
    if subject== "c"
        return 3
    if subject== "d"
        return 4
    if subject== "e"
        return 5
    if subject== "f"
        return 6

def studyyears():
    studyyears= ("""
How many years you want to study?
a. less than 3
b. 3
c. 4
d. 5
e. 6
(type a,b,c,d,e):
               """)
    if studyyears== "a"
        return 1
    if studyyears== "b"
        return 2
    if studyyears== "c"
        return 3
    if studyyears== "d"
        return 4
    if studyyears== "e"
        return 5

def reading():
    reading= ("""
How do you feel about reading?
a. I hate it
b. It's okay
c. I love it
(type a,b,c):
            """)
    if reading== "a"
        return 1
    if reading== "b"
        return 2
    if reading== "c"
        return 3

def schoolgrade():
    schoolgrade("""
What is your current grade?
a. A-B
b. C
c. D
e. F
(type a,b,c,e):
            """)
    if schoolgrade == "a"
        return 1
    if schoolgrade == "b"
        return 2
    if schoolgrade == "c"
        return 3
    if schoolgrade == "F"
        return 4
