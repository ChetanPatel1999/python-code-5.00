#function with parameter
#paremter :- its just variable which declare after function name
def square(num):
    square=num*num
    print(f"square of {num} = {square}")

def addition(a,b):
    c=a+b
    print("addition = ",c)

def factors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=" ")
    print()

#main program
factors(15)
factors(20)
factors(25)
addition(34,10)
square(3)
square(6)
square(7)