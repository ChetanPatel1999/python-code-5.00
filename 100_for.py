#  Write a program to display factorial of given number. 
n=int(input("enter a num :"))# 5
fact=1
for i in range(1,n+1): # 1 2 3 4 5
    fact=fact*i # 120
print(f"factorial of {n} = {fact}")
