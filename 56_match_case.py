# Write a program to make simple calculator. 
#       Press 1 to addition 
#       Press 2 to subtraction 
#       Press 3 to multiplication 
#       Press 4 to division 

print("<=== welcome to my calculator ===>")
print("     Press 1 for addition ")
print("     Press 2 to subtraction ")
print("     Press 3 to multiplication ")
print("     Press 4 to division ")
num=int(input("     press any num = "))

match num:
    case 1:
        print("this is addition code :")
        a=int(input("enter first num : "))
        b=int(input("enter second num : "))
        c=a+b
        print("addition = ",c)
    case 2:
        print("this is subtraction code :")
        a=int(input("enter first num : "))
        b=int(input("enter second num : "))
        c=a-b
        print("subtraction = ",c)    
    case 3:
        print("this is multiplication code :")
        a=int(input("enter first num : "))
        b=int(input("enter second num : "))
        c=a*b
        print("multiplication = ",c)      
    case 4:
        print("this is division code :")
        a=int(input("enter first num : "))
        b=int(input("enter second num : "))
        c=a/b
        print("division = ",c)          
    case _:print("please press 1 to 4")    