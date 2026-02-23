x=4
print(x)
def hello():
    x=5
    print("The local x is",x)
    print("Hello harryy")
hello()
print("the global x is",x)

y=10
def my_function():
    global y
    y=20
    print(y)
my_function()
print(y)
