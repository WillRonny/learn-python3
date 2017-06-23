import json
def get_stored_usernames():
	#如果存储了用户。就获取他
	file_name = 'username.json'
	try:
		with open(file_name) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username


def get_new_username():
	username = input('what your name:')
	file_name = 'username.json'
	with open(file_name,'w') as f_obj:
		json.dump(username,f_obj)
	return username


def greet_user():
	username = get_stored_usernames()
	if username:
		print('welcom back'+username)
	else:
		get_new_username()
		print('We will remember you when you come back ' + 'username' + '!')

greet_user()

