# Write a program to display table of given number. 
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
n=int(input("enter a num : "))
i=1
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i+=1 