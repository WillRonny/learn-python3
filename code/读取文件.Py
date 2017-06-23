filename = '文档2.txt'
with open(filename) as file_obj:
	lines = file_obj.readlines()

pi_str = ' '
for line in lines:
	pi_str = line + pi_str
print(pi_str)

