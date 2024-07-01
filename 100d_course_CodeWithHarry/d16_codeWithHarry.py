x = int(input("Enter the value of x: "))
# X is the variable to match.
match x:
    # if x is 0
    case 0:
        print("x is zero.")
    # if case is 4
    case 4:
        print("x is four")
    case _ if x == 3:
        print("x is 3.")
    case _ if x == 2:
        print("x is 2")
    case _:
        print("Invalid Number")