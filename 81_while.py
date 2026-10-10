# Write a program to display factors count of given number.
n=int(input("enter a num : ")) #20
i=1
res=0
while i<=n:
    if n%i==0:  
        res=res+1 
    i+=1 
print(f"total factors = {res}")    