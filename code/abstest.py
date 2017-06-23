def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')   #  判断输入的类型是否满足条件
    if x >= 0:
        return x
    else:
        return -x