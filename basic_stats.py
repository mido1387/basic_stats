# -*- coding: utf-8 -*-
"""
Basic stats, standard deviation function.
Returns length of list, average, and standard deviation.
author: michael dooley
 
"""
def stddev(datalist):
    N=0 
    for i in datalist: 
        N+=1
    avg=sum(datalist)/N
    variance = list(map(lambda x: x - avg, datalist))
    varsquare = list(map(lambda x: x*x, variance))
    n=N-1
    a=sum(varsquare)/(n)
    b=a**0.5
    return N, avg, b
