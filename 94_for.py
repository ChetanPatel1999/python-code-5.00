#  Write a program to display sum 1 to n ( given number). 
n=int(input("enter a num :")) #10
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i 
print(f"sum of 1 to {n} only even numbers = {sum}")