marks=int(input("Enter your marks"))
if(marks>=90):
    print("GRADE A")
else:
    if(marks>70):
        print("GRADE B")
    else:
        if(marks>50):
            print("GRADE C")
        else:
            if(marks>40):
                print("GRADE D")
            else:
                print("FAIL")
