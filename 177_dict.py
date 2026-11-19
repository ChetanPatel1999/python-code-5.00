#membership operators in dictionary
#in :- return true if key is present in dictionary

# student = {101:"ram" ,  102 : "shyam" , 103 : "harish" }
# print(102 in student)
# print("ram" in student.values())


# when we update dictionary value using key so 
#that time if key is not exist in dictonary so that time
#that key:value added in dictionary
# student = {101:"ram" ,  102 : "shyam" , 103 : "harish" }
# print(student)
# student[105]="raj"
# print(student)


#update() method:
# student = {101:"ram" ,  102 : "shyam" , 103 : "harish" }
# print(student)
# # student.update({102:"raj"}) # update
# # student.update({105:"raj"}) # added it in last
# student.update({105:"raj",106:"ramesh"}) # added it in last
# print(student)


# delete element from dictionary
# pop(key):
# student = {101:"ram" ,  102 : "shyam" , 103 : "harish" }
# print(student)
# student.pop(102)
# print(student)

#popitem():- delte last element
# student = {101:"ram" ,  102 : "shyam" , 103 : "harish" }
# print(student)
# student.popitem()
# print(student)


# del :- 
# student = {101:"ram" ,  102 : "shyam" , 103 : "harish" }
# print(student)
# # del student   #delete complete dictionary
# del student[102]   #delete complete dictionary
# print(student)

#clear() : delete all elemnet but not dictionary
# student = {101:"ram" ,  102 : "shyam" , 103 : "harish" }
# print(student)
# student.clear()
# print(student)


# copy():-
# student = {101:"ram" ,  102 : "shyam" , 103 : "harish" }
# s1=student.copy()
# print(student)
# print(s1)

# s1[101]="raj"

# print(student)
# print(s1)
