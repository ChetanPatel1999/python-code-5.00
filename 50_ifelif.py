# Write a program to find greatest number among has given three numbers. 
a=int(input("enter value of a = "))#56
b=int(input("enter value of b = "))#69
c=int(input("enter value of c = "))#13
if a>b and a>c:
    print("greatest num = ",a)
elif b>c:
    print("greatest num = ",b)
else:
    print("greatest num = ",c)    
