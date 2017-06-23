#int('123456',base = 8)
import functools
int2 = functools.partial(int,base = 2)    #base = 2 也可以用dict来表示   **kw 
print(int2('100010'))    #输入的这个数是二进制的
# 输出34
max2 = functools.partial(max, 10)
print(max2(2,3,4))
#输出  10,2,3,4