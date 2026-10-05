# 2. Write a program using switch-case to check whether a given number is 
# even or odd. 
num=int(input("enter a num : ")) # 19
match num%2==0:
    case True:print("num is even")
    case False:print("num is odd")