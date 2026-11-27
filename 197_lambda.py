# Lambda  function

# def add(a,b):
#     c=a+b
#     return c

printMsg = lambda : print("hello students")
add = lambda a,b : a+b
square= lambda num : num*num
cube= lambda num : num*num*num
areaOfCircle = lambda radius : 3.141*radius*radius
evenOdd = lambda num : "even" if num%2==0 else "odd"
evenlist= lambda l1 : [n for n in l1 if n%2==0 ]

greatest = lambda a,b : a if a>b else b

#main program

print("greatest num = ",greatest(45,7))
l1=[3,5,4,6,7,8]
l2 = evenlist(l1)
print(l2)

print(evenOdd(8))

printMsg()
print("sum = ",add(12,6))
print("square = ",square(6))
print("cube = ",cube(6))
print("areaOfCircle = ",areaOfCircle(6))
