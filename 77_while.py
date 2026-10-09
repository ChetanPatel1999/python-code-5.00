#  Write a program to display sum 1 to n ( given number). 
n=int(input("enter a num : ")) # 6
i=1
res=0
while i<=n:
    res=res+i  
    i+=1 
print(f"sum of 1 to {n} = {res}")    
print(f"average of 1 to {n} = {res/n}")    