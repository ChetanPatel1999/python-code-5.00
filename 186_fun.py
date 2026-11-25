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

def multiplication():
    a=int(input("enter a = "))
    b=int(input("enter b = "))
    c=a*b
    print("multiplication = ",c)

def division():
    a=int(input("enter a = "))
    b=int(input("enter b = "))
    c=a/b
    print("division = ",c)

num=int(input("enter a num : "))
match num:
    case 1:addition()
    case 2:subtraction()
    case 3:multiplication()
    case 4:division()
    case _: print("please enter 1 to 4")