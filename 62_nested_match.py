#club mini project
age=int(input("enter your age : ")) # 15
if age>=18:
    print("<=== welcome to my club ===>")
    print("club menue :")
    print("1. Noodles : 180")
    print("2. Burger : 100")
    print("3. French fries : 120")
    order=int(input("please order : ")) # 5
    match order:
        case 1: print("your Noodles is ordered please pay 180 rs") 
        case 2: print("your Burger is ordered please pay 100 rs")
        case 3: print("your French fries is ordered please pay 120 rs")   
        case _: print("please enter 1 to 3 for order")
else:
    print(f"you are not allowed please try after {18-age} year")    