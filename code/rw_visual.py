import matplotlib.pyplot as plt
from random_walk import RandomWalk

#创建一个RandomWalk的实例，并将其包含的点都绘制出来

while True:
	rw = RandomWalk()
	rw.fill_walk()
	plt.scatter(rw.x_value,rw.y_value,s = 15)

	plt.show()

	keep_running = input('Make anather walk?(y/n)')
	if keep_running == 'n':
		break
		