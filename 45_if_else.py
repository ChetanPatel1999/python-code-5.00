# Write a program to check whether a character is an alphabet or not. 
ch= input("enter a character = ") # b
if ord(ch) in range(97,123) or ord(ch) in range(65,91):
    print("char is alphabet")
else:
    print("char is not alphabet")    

