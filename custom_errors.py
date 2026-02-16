a=int(input("enter any value(5-9)"))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
