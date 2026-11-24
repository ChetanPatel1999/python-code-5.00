def addition():
    a=int(input("enter a = "))
    b=int(input("enter b = "))
    c=a+b
    print("addition = ",c)


def subtraction():
    a=int(input("enter a = "))
    b=int(input("enter b = "))
    c=a-b
    print("subtraction = ",c)  


def square():
    num=int(input("enter a num : "))
    square=num*num
    print(f"square of {num} = {num*num}")

#main program
# addition() 
# addition()
# addition()
# addition()
# addition()

square()

for i in range(5):
    addition()
    print("-----------")