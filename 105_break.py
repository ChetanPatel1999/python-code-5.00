#Write a program to display factors count of given number.
n=int(input("enter a num :")) # 444
c=0
for i in range(1,n+1):
    if n % i ==0:
        c+=1
    if c>2:
        break    

if c==2:
    print("num is prime")
else:
    print("num is not prime")    