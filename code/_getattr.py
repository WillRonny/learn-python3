#很多动态的调用  很重要
#要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__get#attr__()方法，动态返回一个属性。  很有用
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
print(s.score)
print(s.age())
# AttributeError: 'Student' object has no attribute 'grade'
print(s.grade)