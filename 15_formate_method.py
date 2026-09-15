# print output using format method
a=12
b=5
c=a+b
h=5.6
name="ram sharma"
city="indore"
print("sum of {} and {} = {}".format(a,b,c))
print("sum of {0} and {1} = {2}".format(a,b,c))
print("sum of {1} and {1} = {1}".format(a,b,c))
print("sum of {x} and {y} = {z}".format(x=a,y=b,z=c))
print("name of student = {}".format(name))
print("height of student = {}".format(h))
print("my birth place is {0} and also my education place is {0}".format(city))