#Write a program to display factors count of given number.
n=int(input("enter a num :")) # 6
sum=0
for i in range(1,n+1):
    if n % i ==0:
        sum=sum+i
if sum== n*2:
    print("perfact number")
else:
    print("not perfact num")
