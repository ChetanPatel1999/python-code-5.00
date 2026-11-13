# wap to create a list of sqaure from the given list.
#list comprehension:-List comprehension offers a shorter syntax when you want to create a new list based 
# on the values of an existing list.  

#without list comprehension
# l1= [2,4,3,5,6,7]
# l2=[]
# for n in l1:
#     l2.append(n*n)

# print(l1)
# print(l2)

#with list comprehension
# l1=[2,4,3,5,6,7]
# l2 =[n*n for n in l1]
# print(l1)
# print(l2)




#wap to make a new list from existing list and new list have only even numbers.
# l1=[5,9,3,4,7,8,12,45]
# l2=[]
# for n in l1:
#     if n%2==0:
#         l2.append(n)
# print(l1)        
# print(l2)   

#with list comprehension
# l1=[5,9,3,4,7,8,12,45]
# l2=[n for n in l1 if n%2==0]
# print(l1)        
# print(l2)     
# 


# # list comprehension
# l1=[5,9,3,4,7,8,12,45]
# l2=[n for n in l1 if n%5==0]
# print(l1)        
# print(l2) 


# # list comprehension
# l1=[5,9,3,4,7,8,12,45]
# l2=[n for n in l1 if n>10]
# print(l1)        
# print(l2) 


# # list comprehension
# l1=[5,9,3,4,7,8,12,45]
# l2=[n for n in l1 if n<10 and n>5]
# print(l1)        
# print(l2) 


# list comprehension
# l1=[5,9,3,4,7,8,12,45]
# l2=[n*n for n in l1 if n<10 and n>5]
# print(l1)        
# print(l2) 


#without list comprehension
# l1=["apple","banana","mango","orange","watermelon"]
# l2=[]
# for word in l1:
#     if 'm' in word:
#         l2.append(word)
# print(l1)        
# print(l2)        


#list comprehension
# l1=["apple","banana","mango","orange","watermelon"]
# l2=[word for word in l1 if 'm' in word]
# print(l1)        
# print(l2)     
# 

# make a list containing even number 1 to 20 using list comprehension.
# l1=[n for n in range(1,21) if n%2==0]
# print(l1)




# #list comprehension
# l1=["apple","banana","mango","orange","watermelon"]
# l2=[len(word) for word in l1 if 'm' in word]
# print(l1)        
# print(l2)    
# 

# #list comprehension
# l1=["apple","banana","mango","orange","watermelon"]
# l2=[len(word)*2 for word in l1 if 'm' in word]
# print(l1)        
# print(l2)   


#list comprehension
# l1=["apple","banana","mango","orange","watermelon"]
# l2=[len(word)**2 for word in l1 if 'm' in word]
# print(l1)        
# print(l2)   

