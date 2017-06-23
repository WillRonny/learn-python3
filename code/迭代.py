 from collections import Iterable           
isinstance('abc', Iterable) # str是否可迭代
#True
isinstance([1,2,3], Iterable) # list是否可迭代
#True
isinstance(123, Iterable) # 整数是否可迭代
#False



#下表循环怎么办
for i,value in enumerate (['a','b','b']):
	print(i,value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
     print(x, y)