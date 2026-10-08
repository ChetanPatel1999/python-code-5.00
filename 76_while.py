#  Write a program to display multiple of   7  between given range.
i=int(input("enter starting range :  "))# 12
n=int(input("enter a ending range : "))# 25
while i<=n: 
    if i%2==0:
        print(i,end=" ") # 4 8
    i+=1 #6