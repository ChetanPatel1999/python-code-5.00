#  Calculate power of a number without using pow(). 
n=int(input("enter a num :"))
p=int(input("enter a power :"))

# print("result = ",n**p)
# print("result = ",pow(n,p))

res=1
for i in range(1,p+1):
    res=res*n

print("result = ",res)

