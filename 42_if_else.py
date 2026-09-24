# rite a program to check given number is divisible by 3, 4 and 8 or not. 
num=int(input("enter a num : "))
if num%3==0 and num%4==0 and num%8==0:
    print("num is divisible by 3,4,8")
else:
    print("num is not divisible by 3,4,8")    