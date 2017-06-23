def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)   #  **kw相当于加了一个dict   
person('weir',20)
person('weir',20,city = 'chengdu')

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)  # *args相当于加了一个tuple

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

def person1(name, age, *, city, job):
    print(name, age, city, job)
person1('Jack', 24, city='Beijing', job='Engineer')