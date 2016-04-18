def avg(a,b,c,d,e):
    return (a+b+c+d+e)/2

def range0(a):
    if a <0.0 or a>10.0:
        print a, "is out of range"
    
def output(avg1,avg12):
    out=""" 
The average is {}.
The interger part of the average is {}.
The interger part is {}.
""".format(avg1,avgfirst)
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
    avg12= int(avg1)

    out= output(avg1,avg12)   
    print out

main()
 
