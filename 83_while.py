#Write a program to check given number is perfact or not. 
n=int(input("enter a num : ")) #12
i=1
res=0
while i<=n:
    if n%i==0:   # 1 2 3 6
        res=res+i #12
    i+=1 
if res == n*2:
    print("perfact number")
else:
    print("not perfact number")


