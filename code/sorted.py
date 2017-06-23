from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))    #按照字母排序，必须写第一句引入工具包
print(sorted(students, key=lambda t: t[1]))   #对tuple里的第二个元素进行排序        
print(sorted(students, key=itemgetter(1), reverse=False))    #对数字进行排序	reserve就是对他进行反向排序，可以自己选择true 或者 false
