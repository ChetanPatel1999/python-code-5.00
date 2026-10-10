# Write a program to check given number is prime or not.
n=int(input("enter a num : ")) #23
i=1
res=0
while i<=n:
    if n%i==0:  
        res=res+1 
    i+=1 
if res==2:
    print("num is prime")
else:
    print("num is not prime")    
