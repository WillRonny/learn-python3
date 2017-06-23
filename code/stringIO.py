from io import StringIO

#write to StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())	   #用get.value读取写入后的str

#read from StringIO
f = StringIO('床前明月光，\n疑是地上霜。')
while True:
	s = f.readline()
	if s =='':
		break
	print(s.strip())