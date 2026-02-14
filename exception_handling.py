a=input("ENTER A NUMBER : ")
print(f"THE MULTIPLICATION TABLE OF {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
print("program has ended")

#Error objects
try:
    num=int(input("Enter a number"))
    a=[3,5]
    print(a[num])
except ValueError:
    print("Number enterd is not a integer")
except IndexError:
    print("Invalid index")
