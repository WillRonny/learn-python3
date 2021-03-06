from random import choice

class RandomWalk():
	"""生成一个生成随机漫步的类"""
	def __init__(self, num_point = 5000):
		self.num_point = num_point

		self.x_value = [0]
		self.y_value = [0]

  #使用fill_walk生成漫步包含的点
	def fill_walk(self):
		#不断漫步，直到列表达到指定长度
		while len(self.x_value)<self.num_point:

			#设计前进方向和前进距离
			x_direction = choice([1,-1])
			x_distance = choice([0,1,2,3,4])
			x_step = x_direction*x_distance

			y_direction = choice([1,-1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction*y_distance

			if x_step == 0 and y_step == 0:
				continue
			
			#这里的[-1]代表的是x_value 的最后一个值
			next_x = self.x_value[-1] + x_step
			next_y = self.y_value[-1] + y_step

			self.x_value.append(next_x)
			self.y_value.append(next_y)
