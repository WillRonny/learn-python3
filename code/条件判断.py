age = 22
if age >=  18:
	print('Adult')
else:
	prinr('小屁孩')   # if 和 else 要用：

if 2:
	print('True')	
 
s = input('birth:')
birth = int(s)       #input返回的数据类型是str,因此需要类型转换一波
if birth < 2000:
	print('00前')
else:
	print('00后')	



h = input('height:')
w = input('weight:')
height = float(h)
weight = float(w)
bmi = weight/(height*height)
if bmi < 18.5:
	print('过轻')
elif (bmi >= 18.5)and(bmi <28):
	print('肥胖')   
else :
	print('过度肥胖')