# import random
# mat=[]
# row=3
# col=2
# for i in range(row):
#     r=[]
#     for j in range(col):
#         r.append(random.randint(11,100))
#     mat.append(r)


# print("display matrix : ")
# for row in mat:
#     for ele in row:
#         print(ele,end=" ")
#     print()    


# max=mat[0][0]   
# for row in mat:
#     for ele in row:
#         if max<ele:
#             max=ele

# print("max element : ",max)


import numpy 
matrix = numpy.random.randint(11, 100, (3, 3))
print(matrix)
print("max = ",numpy.max(matrix))


