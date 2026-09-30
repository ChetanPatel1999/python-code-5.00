#wap to print state full according short name of state.
state=input("enter state short name = ") # up
match state:
    case "mp" : print("madhya-pradesh")
    case "up" : print("uttar-pradesh")
    case "gj" : print("gujrat")
    case "rj" : print("rajsthan")
    case "uk" : print("utrakhnad")
    case "mh" : print("mharashtra")
    case _ :print("please enter right short name")
