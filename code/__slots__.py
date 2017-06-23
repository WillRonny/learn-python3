#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
	__slots__ = ('name','age')

class GStudent(object):
	"""docstring for GStudent"""
	pass

s = Student()
s.name = 'Ronny'
s.age = 20
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GStudent()
g.score = 99
print('g.score = ',g.score)


