# set methods ():-

# union(), update ()
# s1={3,4,5,6}
# s2={5,6,7,8}
# print(s1)
# print(s2)
# # s1.update(s2)
# # s2.update(s1)
# s3= s1.union(s2)
# print(s1)
# print(s2)
# print(s3)

# #intersection() , intersecion_update()
# #keep duplicate values 
# s1={3,4,5,6}
# s2={5,6,7,8}    
# # s3=s1.intersection(s2)
# # s1.intersection_update(s2)
# s2.intersection_update(s1)
# print(s1)
# print(s2)
# # print(s3)


#symmetric_difference()  , symmetric_difference_update() 
#not keep duplicate value both set
# s1={3,4,5,6}
# s2={5,6,7,8}    
# # s3=s1.symmetric_difference(s2)
# # s1.symmetric_difference_update(s2)
# s2.symmetric_difference_update(s1)
# print(s1)
# print(s2)
# # print(s3)


#difference(),difference_update()
# s1={3,4,5,6}
# s2={5,6,7,8}  
# # s3=s1.difference(s2)
# # s3=s2.difference(s1)
# # s1.difference_update(s2)
# s2.difference_update(s1)
# print(s1)
# print(s2)
# # print(s3)

#issubset()
# s1={2,3,4,5}
# s2={4,5}
# # print(s2.issubset(s1))
# print(s1.issuperset(s2))

#isdisjoint() :- both set have any one value same so ans is false othrwise true
s1={3,4,5}
s2={6,7,8}
print(s1.isdisjoint(s2))