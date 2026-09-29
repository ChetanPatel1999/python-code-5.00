# Given a month number, print the number of days (with Feb as 28 days). 
num=int(input("enter a num for month = "))
if num==2:
    print("28 days")
elif num in (1,3,5,7,8,10,12):
    print("31 days")  
elif num in (4,11,6,9):
    print("30 days")
else:
    print("please enter 1 to 12")

