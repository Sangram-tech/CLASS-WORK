#DICT OPERATION
D1={1:'A',2:'B',3:'C',4:'D',5:'E'}
print(D1)
D1[6]='F'
print(D1)
del D1[6]
print(D1)
print(D1.get(3))
print(D1.keys())
print(D1.values())
print(D1.items())
D1.clear()
print(D1)