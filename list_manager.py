# List manager
import random

def random_order(list1):
    '''returns the list with random order'''
    random.shuffle(list1)
    return list1

def order_by_increasing_value(list1):
    '''returns the list ordered by increasing value'''
    list1.sort()
    return list1

def order_by_decreasing_value(list1):
    '''returns the list ordered by decreasing value'''
    list1.sort(reverse = True)
    return list1

def reverse_order(list1):
    '''returns the list in reverse order'''
    return list1[::-1]


def stringfy_list(list):
    '''returns a list with all elements turned into strings'''
    list_1 = ' '.join([str(elem) for elem in list]) 
    return list_1

def multiply_list(list, multiple):
    '''returns the list with all elements multipled by the value multiple'''    
    list_1 = [ i*multiple for i in list]
    return list_1
    

def get_highest_value(list):
    return max(list)

def get_lowest_value(list):
    return min(list)
    

list_1 = [1, 2, 3, 4]
print(stringfy_list(list_1))
print(multiply_list(list_1,5))
print(get_highest_value(list_1))
print(get_lowest_value(list_1))
