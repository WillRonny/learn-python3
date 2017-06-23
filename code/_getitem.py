#Fib实例虽然能作用于for循环，看起来和list有点像，
#但是，把它当成list来使用还是不行，比如，取第5个元素
class Fib(object):
	"""docstring for Fib"""
	def __getitem__(self, n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a +b
		return a

f = Fib()
print(f[100])