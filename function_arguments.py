#default arguments

def average(a=9,b=1):
    print("The Average is :",(a+b)/2)
average()

def name(fname,mname="JOHN",lname="WATSON"):
    print("HELLO",fname,mname,lname)
name("AMY")

#variable lenght arguments
 
def average(*numbers):
    sum=0
    for i in numbers:
        
        sum=sum+i
    print("AVERAGE IS :",sum /len(numbers))
average(5,5,5)
