#这个是用来过滤序列的
def odd_iter(n):
  return n%2 == 1
L = range(100)
print(list(filter(odd_iter,L)))
