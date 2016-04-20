def avg(a,b,c,d,e):
    return ((a+b+c+d+e)/5)

def range0(a):
    if a <0.0 or a>10.0:
        print a, "is out of range" 
        return a==0

def oddeven(b):
    if b ==1 or b ==3 or b ==5 or b==7 or b==9:
        return "odd"
    else:
        return "even"
    print oddeven


  
def output(avg1,intpart,oddeven1):
    out=""" 
The average is {}.
The interger part of the average is {}.
The interger part is {}.
""".format(avg1,intpart,oddeven1)
    return out
    
def main():
    print "This  program will ask you for 5 integer or float values."
    print "It will calculate the average of all valus from 0 inclusive to 10 exclusive."
    print "It will print out whether the resulting average is even or odd."

    n0= float(raw_input("n0:"))
    range00= range0(n0)
    n1= float(raw_input("n1:"))
    range00= range0(n1)
    n2= float(raw_input("n2:"))
    range00= range0(n2)
    n3= float(raw_input("n3:"))
    range00= range0(n3)
    n4= float(raw_input("n4:"))
    range00= range0(n4)


    avg1= avg(n0,n1,n2,n3,n4)
    intpart= int(avg1)
    oddeven2= oddeven(int(avg1))
    out= output(avg1,intpart,oddeven2)
    print out


main()
 
