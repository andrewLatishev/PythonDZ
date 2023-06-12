#s = [i for i in range(17,60)]
#print(s)
#a = [i**(1/2) for i in range(1,1001)]
#print(a)
#b = [i**(1/2) for i in range(1,1001) if i % 3]
#print(b)
#f = lambda x: x*x
#print(f(-2)) -- 4

#f = lambda x: x if x % 2 else x*x
#print(f(-1), f(-2))

#g = lambda x, y, z: x + y + z
#print(g(3, 4, 5))

#list_ = input('dsbsd').split()
#new_list = list(map(int, list_))
#print(new_list[0] + new_list[1] + new_list[2])

#list_ = list(map(sqrt, range(1, 1001)))
#print(list_)

#list_ = [45, -67, 78, -90, -54]
#new_list = list(filter(lambda x: x > 0, list_))
#print(new_list)
#new_list2 = [x for x in list_ if x > 0]
#print(new_list2)

#from functools import reduce
#print(reduce(lambda x, y: x * y, [3, 4, 5]))
"""import math
list_ = [i**(1/2) for i in range(1, 1001)]
new_list = list(map(lambda x: sin(x*x) + x, list_))
print(new_list)


new_list2 = list(filter(lambda i: i > 10 and i < 20, new_list))
print(new_list2)"""


'''
from functools import reduce
import math
list_ = [math.sqrt(i) for i in range(1000)]
new_list = [math.sin(list_[i]) + list_[i] for i in range(len(list_))]
def func1(n):
    if n > 10 and n < 20:
        return n
flist_ = filter(func1,new_list)
list__ = list(flist_)
def func2(b, c):
    return b * c
llist_ = reduce(func2, list__)
print(llist_)
'''
'''
def func(n):
    m = 0
    print('func: m = ' + str(m))
    m += 1
    return n*n + m*n


def gen(n):
    m = 0
    for m in range(n):
        print('gen: m = ' + str(m))
        yield m*m + m


list1 = [func(i) for i in range(10)]
print(list1)

iterator = iter(gen(10))
for i in range(12):
    print(next(iterator))
# обработка 
'''



