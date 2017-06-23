from functools import reduce   #使用reduce必须要这个 声明
L = [1,2,3,4]
def prod(x,y):
	return x*y
print(reduce(prod,L))	
	