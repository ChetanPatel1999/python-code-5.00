#  Write a program using switch-case to check whether the entered character 
# is a vowel or a consonant.
# alpha=input("enter a alpha = ") # o
# match alpha:
#     case 'a':print("alpha is vovel")  
#     case 'e':print("alpha is vovel")  
#     case 'i':print("alpha is vovel")  
#     case 'o':print("alpha is vovel")  
#     case 'u':print("alpha is vovel")  
#     case _: print("alpha is consonent")



#second way
alpha=input("enter a alpha = ") # o
match alpha:
    case 'a'|'e'|'i'|'o'|'u':print("alpha is vovel")    
    case _: print("alpha is consonent")