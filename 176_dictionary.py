#dictionary methods

#get() :- access values according to key
# student = {101:"ram" ,  102 : "shyam" , 103 : "harish" }
# print(student.get(102))

# for key in student:
#     print(key,student.get(key))

# #keys(): its return all keys of dictionary
# student = {101:"ram" ,  102 : "shyam" , 103 : "harish"}
# print(student.keys())

# #values():- its return all values of dictionary
# print(student.values())


# #items():
# print(student.items())


student = {101:"ram" ,  102 : "shyam" , 103 : "harish" }
# for key in student.keys():
#     print(key)

# for value in student.values():
#     print(value)

# for item in student.items():
#     print(item)

for i,j in student.items():
    print(i,j)

