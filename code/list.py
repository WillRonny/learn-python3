classmates = ['魏荣','彭威','夏盼']
print(classmates[0],classmates[1],classmates[2])    # 0 1 2 代表第一个第二个和第三个
print(classmates[-1])  #  倒数第一个  以此类推 -2 -3是倒数第二个和第三个
classmates.append('许小涛')  #在原数组上追加一个元素
classmates.insert(1,'西瓜')  #在指定的位置插入一元素
classmates.pop()             #删除最后一个元素
classmates.pop(1)            #删除指定的元素
classmates[1] = '丢丢'       #替换
print(classmates)

L = ['爱',123,True]         #列表的元素也可以不一样
#List 中间也可以有另外一个list