import math             #记得导入函数包math
def q(a,b,c):
 d =  b*b-4*a*c
 if d >= 0:
	 x1 = (-b+math.sqrt(d))/(2*a)
	 x2 = (-b-math.sqrt(d))/(2*a)
	 return x1,x2

 else:
	 print("wujie")

   
	
print(q(1,5,3))