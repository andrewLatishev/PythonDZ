#Сравнение скорости выполения математической функции
#Подсчет синуса
import numpy as np
import time
from collections import deque
from array import array

def check_np_array():
    np_array = np.array([11, 25, 51, 19], dtype=int)

    start = time.time()
    for _ in range(1000):
        for num in np_array:
            _ = np.sin(np.pi/num)
    end = time.time()

    return 'Время выполнения функции numpy.array: ' + str(end - start)

def check_array_array():
    array_array = array("i", [11, 25, 51, 19])

    start = time.time()
    for _ in range(1000):
        for num in array_array:
            _ = np.sin(np.pi/num)
    end = time.time()

    return 'Время выполнения функции array.array: ' + str(end - start)

def check_list():
    simple_list = list([11, 25, 51, 19])

    start = time.time()
    for _ in range(1000):
        for num in simple_list:
            _ = np.sin(np.pi/num)
    end = time.time()

    return 'Время выполнения функции list: ' + str(end - start)

def check_deque():
    deque_array = deque([11, 25, 51, 19])

    start = time.time()
    for _ in range(1000):
        for num in deque_array:
            _ = np.sin(np.pi/num)
    end = time.time()

    return 'Время выполнения функции deque: ' + str(end - start)

print(check_nparray())
print(check_arrayarray())
print(check_list())
print(check_deque())
