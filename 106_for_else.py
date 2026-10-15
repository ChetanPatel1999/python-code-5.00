# if break execute so else not execute
# but if break is not execute so else must execute
for i in range(1,11):
    if i==5:
        break
    print(i)
else:
    print("else is exicute")    