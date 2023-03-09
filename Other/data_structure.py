#import array

#array_ = array.array('i', [3, 4, 5])
#print(array_)

import collections

deque_ = collections.deque()
deque_.append('abc')
deque_.append('def')
deque_.append('fgh')
print(deque_)
print(deque_.pop(), deque_)
deque_.appendleft('ikl')
deque_.appendleft('mno')
print(deque_)
deque_.popleft()
print(deque_)
