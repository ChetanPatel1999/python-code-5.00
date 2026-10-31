# upper() :- its convert string in upercase
# name="ram sharma"
# print(name)
# name=name.upper()
# print(name)


# code to conver lower case string to uper case
# name="my56 name34 is chetan"
# s=""
# for ch in name: # c
#     if ch>='a' and ch<='z':
#         s = s + chr(ord(ch)-32)
#     else:
#         s=s+ch   
        
# print(name)        
# print(s)    


#lower():- convert string to lower case
# name="RAMAYAN"
# s=name.lower()
# print(name)
# print(s)


#strip() :- remove white space around string
# s="   hello ji      "
# print(s)
# s=s.strip()
# print(s)


#replace() :- replace some pasrt of string
# s="this is indore city"
# print(s) 
# s=s.replace("indore","ujjain")
# s=s.replace("indore","t")
# print(s)


#capitalize():- first char make capitle
# s="the jangle book"
# print(s)
# s=s.capitalize()
# print(s)


#title():- each word first char make capitle
# s="the jangle book"
# print(s)
# s=s.title()
# print(s)


# startwith():- 
# name=input("enter your name : ")

# if name.startswith("mr."):
#     print("valid name")
# else:
#     print("your name is not valid")    


# endswith():- 
# name=input("enter your gmail : ")

# if name.endswith("@gmail.com"):
#     print("valid gmail")
# else:
#     print("not valid gmail")    


#isupper():
# islower():-
# s="Ram"
# if s.isupper():
#     print("string is upper case")
# else:
#     print("string is not upper case")    


# istitle()
# s="The man"
# print(s.istitle())

#isalpha():-
# s=input("enter a string = ")
# if s.isalpha():
#     print("string is alphabetic")
# else:
#     print("string is not alphabatic")    


#isdigit()
# s="5357865"
# res=s.isdigit()
# print(res)

#isalnum()
# s="5357865ewqwe"
# res=s.isalnum()
# print(res)

#isidentifire()
# s="hel@lo_123"
# print(s.isidentifier())

#find():- its given index number of passing sub string 
# if substring is not found so its given -1
# s="ramayan"
# print(s.find("th"))

# s=input("enter a string : ")
# sub=input("enter a search string : ")
# if s.find(sub)==-1:
#     print("sub string is not found")
# else:
#     print("sub string is found")    


#index():- its given index number of passing sub string 
# if substring is not found so its given error
# s="this is box"
# print(s.index("ram"))


# isspace():- 
s="    "
print(s.isspace())
