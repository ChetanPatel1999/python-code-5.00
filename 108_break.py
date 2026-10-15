n1=int(input("enter n1 : ")) # 12
n2=int(input("enter n2 : "))# 24
if n1<n2:
    min=n1
else:
    min=n2    

while True:
    if n1 % min==0 and n2 % min==0:
        print("HCF = ",min)
        break
    min-=1 # 11