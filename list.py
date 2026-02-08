marks=[30,40,50,60,65,70,75,80,85,90,95]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(len(marks))
if 60 in marks:
    print("YES")
else:
    print("NO")

print(marks[::2])

#list comprehension
lst=[i*i for i in range(10) if i%2==0]
print(lst)
