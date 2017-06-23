import functools

def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print('begin call, %s %s():'%(text,func.__name__))

                func(*args,**kw)
                print('end call, %s %s()'%(text,func.__name__))

            return wrapper
        return decorator
    else:

            @functools.wraps(text)
            def wrapper(*args,**kw):
                print('begin call, execute %s():' % (text.__name__))
                text(*args,**kw)
                print('end call, execute %s()' % (text.__name__))

            return wrapper



@log('te')        #test = log('te')(test)
def test(a,b):
    print (a+b)
test(1,2)