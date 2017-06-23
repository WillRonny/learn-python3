from math import sqrt
def A(x=[],*func):
	return[f(x_k) for x_k in x for f in func]

print(A([1,2,3,4],abs,sqrt))           #  函数也可以指向一个变量




f = abs
f(-10)
>>>10
