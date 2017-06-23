from datetime import datetime
#with语句来自动帮我们调用close()方法

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:  #读取2进制的文件
    s = f.read()
    print('open as binary for read...')
    print(s)