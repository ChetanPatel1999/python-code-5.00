# Default argument in function: 
def studentdisplay(name,rno=00,city="bhopal"):  # here city parameter have a default argument
    print("student info : ")
    print("name : ",name)
    print("rno : ",rno)
    print("city : ",city)
    print("-------------")


#main program
studentdisplay("ram",101,"indore")
studentdisplay("shyam",102)
studentdisplay("sanjhi",103)
studentdisplay("raj",104,"ratlam")
studentdisplay("rajveer")