import json

#number = [2,4,6]
#filename = 'username.json'
#with open(filename,'w') as f_obj:
#	json.dump(number,f_obj)


filename = 'username.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)
print(numbers)