name1 = ['aa','bb','cc']
print(type(name1))

name2 = ['dd','ee']
print(name1+name2)

name2.extend(name1)
print(name2)
name1.insert(2,name2)
print(name1)
name1.pop()
name1.remove('cc')
print(name1)
del name1[1]
print(name1[1:])