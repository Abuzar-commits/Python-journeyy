#List Methods

l=[1,2,3,2,4,5,6]
print(l)
l.append(8)
print(l)

l2=[12,443,54,65,5,22]
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)
l.reverse()
print(l)
l.index(2)
print(1)
print(l.count(2))
m=l.copy()
m[0]=12
print(m)
m.insert(2,444)
print(m)
l2.extend(m)
print(l2)
k=l+m
print(k)
