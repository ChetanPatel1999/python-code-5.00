# we can return multiple value in python
def operation(num):
    square= num*num
    cube = num*num*num
    return square,cube
   

#main program
s= operation(5)
print("sqaure = ",s[0])
print("cube = ",s[1])

