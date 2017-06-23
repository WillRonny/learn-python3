from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':#这种写法固定
	#让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',)) #tuple单元素的表达方法
    print('Child process will start.')
    p.start()   #启动子程序
    p.join()    #等待子程序运行完，才运行下一个

   	
    print('Child process end.')