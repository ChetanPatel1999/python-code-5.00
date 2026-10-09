#  Write a program to display sum 1 to n  ( given number) only even numbers 
# sum. 
n=int(input("enter a num : ")) # 10
i=1
res=0
while i<=n:
    if i%2==0:
       res=res+i  # 45
    i+=1 
print(f"sum of 1 to {n} only even numbers = {res}")  #  
   