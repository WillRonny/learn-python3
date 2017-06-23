#模糊了对象和函数的界限。
class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name
	def __call__(self):    #用call可以不用传入参数
		print('my name is %s' %self.name)  # 中间不要加逗号

s = Student('Ronny')
s()