class student(object):
	"""docstring for ClassName"""
	def __init__(self, name,score):
		self.name = name
		self.score = score
	def getscore(self):
	    print('%s:%s' %(self.name.title()) ,%(self.score))
Ronny = student('ronny',80)
Ronny.getscore()