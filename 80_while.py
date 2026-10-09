# Write a program to display factors of given number.
n=int(input("enter a num : "))  
i=1
while i<=n:
    if n%i==0:
        print(i,end=" ") # 1 3 5 15
    i+=1    