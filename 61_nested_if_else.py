#club mini project
age=int(input("enter your age : ")) # 34
if age>=18:
    print("<=== welcome to my club ===>")
    print("club menue :")
    print("1. Noodles : 180")
    print("2. Burger : 100")
    print("3. French fries : 120")
    order=int(input("please order : ")) # 17
    if order==1:
        print("your Noodles is ordered please pay 180 rs")
    elif order==2:
        print("your Burger is ordered please pay 100 rs")
    elif order==3:
            print("your french fries is ordered please pay 120 rs")
    else:
         print("please enter 1 to 3 for order")
else:
    print(f"you are not allowed please try after {18-age} year")    