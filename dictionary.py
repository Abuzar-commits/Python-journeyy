dic = {
    "Abuzar":"Human being",
    "Spoon" :"Oject"
    }

print(dic["Abuzar"])
print(dic.get("Abuzar"))
#the difference between these two is the first one will give error if keyy is not present and the .get will return none

print(dic)
# to access all the keys at once
print(dic.keys())
for key in dic:
    print(dic[key])

print(dic.values())
print(dic.items())
