#iterate dictionary each element using loop
student = {101:"ram" ,  102 : "shyam" , 103 : "harish" ,106:"raj" }
print(len(student))
print(type(student))

# prints all key of dictionary
# for s in student:
#     print(s)

# prints value of dictionary
# for s in student:
#     print(student[s])    


#print key values both
for s in student:
    print(s,'--->',student[s])   