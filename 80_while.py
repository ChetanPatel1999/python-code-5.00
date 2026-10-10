# Write a program to display factors of given number.
n=int(input("enter a num : ")) #20
i=1
print(f"factors of {n} = ",end="")
while i<=n:
    if n%i==0:  
        print(i,end=" ") #
    i+=1  #8