

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b                    #yield和print类似，但是性质不同
        a, b = b, a + b        #这是一个赋值语句
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:                    #这里并不懂
        print('Generator return value:', e.value)
        break