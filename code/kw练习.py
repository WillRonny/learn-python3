
def print_scores(**kw):  # kw是接受dict的  输出方式看下面
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
        print()    #  这一行谁让输出的每行有间距  原来如此
    #print(kw)        #注意输出的是kw  不是**kw

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,    #是以个dict文件
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)  




##*后面的参数就是表面关键参数，在函数输入里输入就有区别于前面的
def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)        