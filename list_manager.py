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
    pass

def multiply_list(list, multiple):
    '''returns the list with all elements multipled by the value multiple'''
    pass

def get_highest_value(list):
    '''returns the highest value of the list'''
    pass

def get_lowest_value(list):
    '''returns the lowest value of the list'''
    pass

