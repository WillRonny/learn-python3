#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
#该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__
#__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a,self.b = 0,1   #初始化
	def __iter__(self):
		return self           #实例本身就是迭代对象，故返回本身
	def __next__(self):
		self.a,self.b = self.b,self.a +self.b
		if self.a> 100000:
			raise StopIteration(); #退出循环条件
		return self.a

for n in Fib():
	print(n)
