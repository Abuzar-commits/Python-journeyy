ep1={122:45,123:89,567:69,678:69}
ep2={222:67,566:90}
ep1.update(ep2)
print(ep1)
e3={12:54,23:33}
e3.clear()
print(e3)
empt={}
print(empt)
ep1.pop(566)
print(ep1)
#pop.item removes the last item
ep1.popitem()
print(ep1)
#del deletes the entire dictionary but if we give a key it will delete only that pair
del ep1[122]
print(ep1)
