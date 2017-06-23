L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s,str)]    #没想到可以直接在前面和后面加上条件
print(L2)


print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])  #......太简单了吧
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])