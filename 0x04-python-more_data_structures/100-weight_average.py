#!/usr/bin/python3
def weight_average(my_list=[]):
    count = 0
    summ = 0
    if my_list:
        for (x, y) in my_list:
            summ += (x * y)
            count += y
        average = summ / count
        return (average)
    else:
        return (0)
