class Province(object):
	"""docstring for Province"""
	def __init__(self, proname):
		self.proname = proname
	def ps(self):
		print('i am in %s' %self.proname)

class City(Province):
	def __init__(self,proname,cityname):
		Province.__init__(self,proname)
		self.cityname = cityname
	def psl(self):
		print('i am in　%s %s'%(self.proname,self.cityname))

def f(x):
	x.ps()
	x.psl()

f(City('Hubei','wuhan'))


	
		