# Check if a number is even-positive, even-nagative ,odd-positive ,odd
# nagative or zero. 

num=int(input("enter a num : ")) # -55
if num==0:
    print("num is zero")
elif num%2==0:
    if num>0:
        print("even - positive")  
    else:
        print("even - nagative")    
else:
    if num>0:
        print("odd - positive")
    else:
        print("odd - nagative")    
