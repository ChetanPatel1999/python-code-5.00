def add(a,b):
    c=a+b
    return c

def areaOfCircle(radius):
    return 3.141*radius*radius

def factorial(num): # 5
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact



#main program
# print(add(5,9))
res=add(5,9)
print(res)
print("circle area = ",areaOfCircle(4.5))


ans=factorial(5)
print(ans)


r=ord('A')
print(r)

