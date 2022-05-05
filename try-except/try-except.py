while True:
    x = (input("Please enter a number: "))
    y = (input("Please enter a number: "))
    try:
        x = float(x)
        y = float(y)
        print("Division:", x / y)
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...".format(x,y))
    except:
        print("invalid entry!")
        pass





