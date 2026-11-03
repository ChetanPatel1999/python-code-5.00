#  Write a program to find the sum of all elements in an list.
l1=[4,3,6,5,7]
print("list : ",l1)

sum=0
for num in l1: #7
    sum=sum+num # 25

print("list element sum = ",sum)    
print("list element average = ",sum/len(l1))    
if sum%2==0:
    print("sum is even")
else:
    print("sum is odd")    
