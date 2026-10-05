#wap to convert upercase char in lower-case char or
# if input char is lower-case so convert in uper case.
# t  ---> T
# Q  ----> q
ch=input("enter a alphabet = ") # Z
match ch>='a' and ch<='z':
    case True:
       ch= chr(ord(ch)-32)
       print("uper-case = ",ch)
    case False:
       match ch>="A" and ch<"Z":
          case True:
            ch=chr(ord(ch)+32)
            print("lower-case = ",ch)
          case False:
             print("not a valid char")  
          
   
