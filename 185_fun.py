def fun1():
    print("this is fun1")

def fun2():
    print("this is fun2")
    fun1()


def fun3():
    fun2()
    print("this is fun3")    

#main program
fun3()  
print("program is end")  