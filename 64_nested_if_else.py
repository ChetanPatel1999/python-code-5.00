# 2. Check whether a character is a vowel, consonant, or not an alphabet. 
ch=input("enter a character : ") # i
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    if ch in "aeiouAEIOU":
        print("alpha is vovel")
    else:
        print("alpha is consonent")    
else:
    print("char is not alphabet")
