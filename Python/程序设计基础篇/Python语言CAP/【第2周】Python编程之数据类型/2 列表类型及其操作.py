vlist = [0,1,2,3,4]
print(vlist*2)
print(len(vlist[2:]))
for i in vlist[:3]:
    print(i)
print(2 in vlist)
vlist.append(100)
vlist.append(99)
print(vlist)
vlist.sort()
print(vlist)
vlist.reverse()
print(vlist)

print(vlist.index(3))

vlist.insert(3,88)
print(vlist)

print(vlist.count(100))

vlist.remove(100)
print(vlist)

print(vlist.pop(0))
print(vlist)

print("python is an excellent language".split())
