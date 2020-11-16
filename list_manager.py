# List manager
import random
import statistics
import numpy as np



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


def stringfy_list(list1):
    '''returns a list with all elements turned into strings'''
    list_1 = ' '.join([str(elem) for elem in list1]) 
    return list_1

def multiply_list(list1, multiple):
    '''returns the list with all elements multipled by the value multiple'''    
    list_1 = [ i*multiple for i in list1]
    return list_1
    

def get_highest_value(list1):
    return max(list1)

def get_lowest_value(list1):
    return min(list1)


def mean(list1):
    return statistics.mean(list1)

def median(list1):
    return statistics.median(list1)

def std_deviation(list1):
    return statistics.stdev(list1)


def unique_item(list1):
    unique_one = np.array(list1)
    return np.unique(unique_one)

def most_common(list1):
    common = np.array(list1)
    return np.bincount(common).argmax()

def sum_of_all(list1):
    sum_ofall = np.array(list1)
    return np.sum(sum_ofall)
    


if __name__ == "__main__":
    list_1 = [1, 1, 2, 2, 3, 3, 3, 4]
    print(stringfy_list(list_1))
    print(multiply_list(list_1,5))
    print(get_highest_value(list_1))
    print(get_lowest_value(list_1))
    print(random_order(list_1))
    print(order_by_increasing_value(list_1))
    print(order_by_decreasing_value(list_1))
    print(reverse_order(list_1))
    print(mean(list_1))
    print(median(list_1))
    print(std_deviation(list_1))
