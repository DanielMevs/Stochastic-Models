import numpy as np
import random

def populate(n):
    points = np.arange(1, n+1)
    return points


def binarify(Alist):
    for i in range(len(Alist)):
        Alist[i] = random.randint(0,1)
    return Alist

def binary_negation(Alist):
    for i in range(len(Alist)):
        if Alist[i] == 0:
            Alist[i] = 1
        elif Alist[i] == 1:
            Alist[i] = 0
    return Alist

def purify(Alist):
    for i in range(len(Alist)):
        Alist[i] = 0
    return Alist


def brute_cartesian(aList):
    i = len(aList)-1
    j = 0
    count = 1 # for initial purified list
    while(i >= 0):
        if(count == 1):
            aList[i] = 1
            aList = purify(aList[:i])
            
            count += 1
            
        else:
            i -= 1
            aList[i] = 1
            count += 1
            j = i+1
            aList[j] = 0
            count+=1
            
            while(j <= len(aList)-1):
                 if(j == len(aList)-1):
                    while(j > i):
                        aList[j] = 1
                        #count+=1
                j = j+i
                    count+=1
                else:
                    aList[j] = 1
                    count+=1
                    aList[j] = 0
                
               
                        
            
            
    return count




x = populate(4)
print(x)

count = brute_cartesian(x)
print('expected answer: 16')
print('actual answer: ', count)
            
'''x = binary_negation(x)
print(x)'''
        
    
    
    
