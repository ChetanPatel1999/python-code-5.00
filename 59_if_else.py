#wap to convert upercase char in lower-case char or
# if input char is lower-case so convert in uper case.
# t  ---> T
# Q  ----> q
ch=input("enter a alphabet = ") # Z
if ch>='a' and ch<='z':
    ch= chr(ord(ch)-32)
    print("uper-case = ",ch)
elif ch>='A' and ch<='Z':
    ch=chr(ord(ch)+32)
    print("lower-case = ",ch)
else:
    print("char is not a alphabet")    
