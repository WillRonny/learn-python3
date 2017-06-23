#产生一个无穷的序列  1  3  5  7........
def odd_iter():
	n = 1
	while True :
		n = n+2
		yield n
#定义一个筛子
def not_divisble(n):
	return lambda x:x%n >0

#定义一个生成器，不断返回下一个素数
def primes():
	yield 2                       #因为是从3开始算的  漏掉了2
	it = odd_iter()    #初始序列
	while True:
		n = next(it)   #返回序列的第一个数
		yield n
		it = filter(not_divisble(n),it)

#打印1000以内的素数
for n in primes():
	if n < 1000:
		print(n)
	else:
		break
	