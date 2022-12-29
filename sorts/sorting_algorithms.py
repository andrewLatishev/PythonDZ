import math
import time
import random

NUMBER_OF_ELEMENTS_IN_TEST_LIST = 1000
NUMBER_OF_TESTS = 100
RAND_MAX = 10000


def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_


def BubbleSort(list_):
    swapped = True
    last_index = len(list_)
    while swapped:
        swapped = False
        for index in range(last_index - 1):
            if list_[index] > list_[index + 1]:
                list_[index], list_[index + 1] = list_[index + 1], list_[index]
                swapped = True
        last_index -= 1
    return list_


def sort_check(list_):
    for index in range(len(list_) - 1):
        if list_[index] > list_[index + 1]:
            return False
    return True


def test(func):
    total_timer = 0
    for test_number in range(NUMBER_OF_TESTS):
        test_list = generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST)
        timer = time.time()
        test_list = func(test_list)
        timer = time.time() - timer
        total_timer += timer
        if sort_check(test_list):
            '''print("Required time in test №", test_number + 1, "is", timer, "seconds")'''
        else:
            print("Error in test №", test_number + 1)
    print("Required time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer / NUMBER_OF_TESTS, "seconds")


def search_test(func):
    total_timer = 0
    test_list = sorted(generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST))
    for test_number in range(NUMBER_OF_TESTS):
        timer = time.time()
        search_elem = random.randint(-RAND_MAX, RAND_MAX)
        answer = func(test_list, search_elem)
        timer = time.time() - timer
        total_timer += timer
        if not (search_check(test_list, search_elem, answer)):
            print("Error in test №", test_number + 1)
    print("Required time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer / NUMBER_OF_TESTS, "seconds")


def simple_search(list_, search_elem):
    for index in range(len(list_)):
        if list_[index] == search_elem:
            return index
    return None


def insertion_sort(list_):
    for index in range(1, len(list_)):
        i = index
        t = list_[i]
        while i > 0 and t < list_[i - 1]:
            list_[i] = list_[i - 1]
            i -= 1
        list_[i] = t
    return list_


def insertion_binary_sort(list_):
    for index in range(len(list_)):
        i = list_[index]
        l = 0
        r = index - 1
        while l < r:
            middle = (r + l) // 2
            if i < list_[middle]:
                r = middle
            else:
                l = middle + 1
        for j in range(index, l + 1, -1):
            list_[j] = list_[j - 1]
        list_[l] = i
    return list_


list_ = [500, 9, 10, 5, 2, 4, 7, 435]
def quick_sort(list_):
    if len(list_) <= 1:
        return list_
    else:
        s = list_[0]
        left = [i for i in list_ if i < s]
        m = [i for i in list_ if i == s]
        right = [i for i in list_ if i > s]
        return quick_sort(left) + m + quick_sort(right)


print(quick_sort(list_))


def selection_Sort(n):
    for i in range(len(n) - 1):
        m = i
        for j in range(i + 1, len(n)):
            if n[j] < n[m]:
                m = j
        n[i], n[m] = n[m], n[i]
    return n


def binary_search(list_, search_elem):
    search_left = 0
    search_right = len(list_) - 1
    while search_left < search_right:
        search_middle = (search_left + search_right) // 2
        if search_elem > list_[search_middle]:
            search_left = search_middle + 1
        elif search_elem < list_[search_middle]:
            search_right = search_middle - 1
        else:
            return search_middle
    if search_left == search_right:
        if list_[search_left] == search_elem:
            return search_left
        else:
            return None
    return None


def merge(list1, list2):
    index1 = 0
    index2 = 0
    list_ = []
    while (index1 < len(list1)) and (index2 < len(list2)):
        if list1[index1] < list2[index2]:
            list_.append(list1[index1])
            index1 += 1
        else:
            list_.append(list2[index2])
            index2 += 1
    while index1 < len(list1):
        list_.append(list1[index1])
        index1 += 1
    while index2 < len(list2):
        list_.append(list2[index2])
        index2 += 1
    return list_


def merge_sort(list_):
    if len(list_) > 2:
        middle = len(list_) // 2
        list_[:middle] = merge_sort(list_[:middle])
        list_[middle:] = merge_sort(list_[middle:])
        m_list = merge(list_[:middle], list_[middle:])
        return m_list
    elif len(list_) == 2:
        s = max(list_)
        list_[0] = min(list_)
        list_[1] = s
        #print(list_)
        return list_
    else:
        return list_


def search_check(list_, search_elem, answer):
    if answer == None:
        for index in range(len(list_)):
            if list_[index] == search_elem:
                return False
        return True
    else:
        """
        for index in range(answer):
            if list_[index] == search_elem:
                return False
        """
        if list_[answer] == search_elem:
            return True
        else:
            return False


test(selection_Sort)
#test(merge_sort)
#test(insertion_sort)
#test(insertion_binary_sort)
# search_test(binary_search)
# search_test(simple_search)
# test(BubbleSort)
