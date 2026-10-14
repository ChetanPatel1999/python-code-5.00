# .Write a program to display factors of given number. 
# 12 :- 1 2 3 4 6 12
# 15 :- 1 3 5 15
n=int(input("enter a num :")) # 15
c=0
for i in range(1,n+1):
    if n % i ==0:
        c+=1

print(f"factors count = {c}")