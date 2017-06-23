#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log           #相当于执行了  now = log(now)
def now():
    print('a = 2016')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)          #   这一句很重要，在定义wraps函数前记得加 后面会讲
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')           #函数输入参数的     logger('DEBUG')today()   先执行的logger('DEBUG')  返回的是 decorator  然后执行的是decorator（today）
def today():
    print('2015-3-25')

today()
print(today.__name__)