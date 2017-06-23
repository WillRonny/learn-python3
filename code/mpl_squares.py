import matplotlib.pyplot as plt
input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_value,squares,linewidth=5)

#设置坐标轴
plt.title('Squares Numbers',fontsize = 24)
plt.xlabel('value',fontsize = 14)
plt.ylabel('Square of value',fontsize = 14)

#设置刻度标尺的大小 刻度的样式一致
plt.tick_params(axis = 'both',labelsize=14)   
plt.show()