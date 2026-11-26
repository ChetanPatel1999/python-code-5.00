#Variable-Length Arguments  
# *args -These are Non-Keyword Arguments 
def fun(*a):
    print("a = ",a)

def add(*a):
    sum=0
    for n in a:
        sum=sum+n
    print("sum = ",sum)    

def myfun(a,*b):
    print(a,b)
    


#main program
myfun("ram",56,78,90)
fun(12,6,2)
add(4,5,10,20,30)
add(34,78)
add(8,7,6)