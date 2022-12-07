#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    summ = 0
    for i in my_list:
        if i not in uniq:
            uniq.append(i)
    for j in range(len(uniq)):
        summ = summ + uniq[j]
    return (summ)
