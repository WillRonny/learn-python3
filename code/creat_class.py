def fn(self,name = 'world'):
	print('Hello,5%% %s' %name)
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
#要创建一个class对象，type()函数依次传入3个参数：

#class的名称；
#继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

Hello = type('Hello',(object,),dict(hello=fn))   # 创建Hello class


h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello)=',type(Hello))
print('type(h)=',type(h))
