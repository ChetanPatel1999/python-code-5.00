# Wap to find greatest number among has given three numbers without 
# using logical and operator.
a=int(input("enter value of a = "))#56
b=int(input("enter value of b = "))#69
c=int(input("enter value of c = "))#13
# a=45  b=6  c=90 
if a>b:
    if a>c:
        print("max = ",a)
    else:
        print("max = ",c)    
else:
    if b>c:
        print("max = ",b)
    else:
        print("max = ",c)     

  
