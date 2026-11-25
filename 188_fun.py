# function with parameter and  return value
def square(num):
    s=num*num
    return s

def length(l1):
    c=0
    for i in l1:
        c+=1
    return c     

#main program

res = square(2)
if res>10:
    print("hello")
else:
    print("by")    
print("my ans is = ",res)

print("my result is = ",square(9))


l1=[34,56,78,77]
print(length(l1))





