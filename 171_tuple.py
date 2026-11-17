#how to change tuple item 
t1=(4,67,89,23)
print(t1)
l1=list(t1)   # change tuple in list
l1[2]=500 # change value in list
t1=tuple(l1) #v again list convert in tuple 
print(t1)

del t1  # delete tuple completely

print(t1)