# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 09:15:57 2018

@author: lokesh.r
"""
"""
Write a function to find moving average in an array over a window:
Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.
"""
import numpy as np

data =np.array([3,5,7,2,8,11])
s = data.size
def dataSumm(avg):
    data =np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
    print(data)
    sz = data.size
    for i in range(sz):
        if ((data[i:avg+i].size) >= avg):
            
            print(data[i:avg+i], (data[i:avg+i].sum())/avg , sep="=")
            
        
        
dataSumm(3)
