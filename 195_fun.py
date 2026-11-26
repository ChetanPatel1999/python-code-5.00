#Variable-Length Arguments  
# **kargs -These are Keyword Arguments 

# def fun(**a):
#     print(a)  #{"name":"ram","age":15,"city":"indore"}


# fun(name="ram",age=15,city="indore")

def studentDisplay(**student):
    print("student info : ")
    for key in student:
        print(f"{key} : {student[key]}")
    print("-------------")    


studentDisplay(name="raj",age=20)
studentDisplay(name="shyam",age=25,rno=102,city="indore")
studentDisplay(name="hariom",rno=103)

