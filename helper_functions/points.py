import numpy as np
import random

def populate(n):
    points = np.arange(1, n+1)
    return points


def binarify(Alist):
    for i in range(len(Alist)):
        Alist[i] = random.randint(0,1)
    return Alist

def binary_convert(d):
        if d == 0:
            d = 1
            return d
        if d == 1:
            d = 0
            return d



def purify(Alist):
    for i in range(len(Alist)):
        Alist[i] = 0
    return Alist

#algorithm that keeps count of all possible ways to arrange binary values in a list of size 4 (2^4) 
def brute_cartesian():
    count = 0
    arr1 = [0,0,0,0]
    count+=1

    arr2 = [1,1,1,1]
    count+=1

    print(arr1,'      ', arr2)

    bi1 = 1 #binary digit for array 1
    bi2 = 0 #binary digit for array 2

    i =0
        

    n =len(arr1)-1
    m = 1

    while(m <= n+1):
        
        while(i <= n-m):
            arr1[i]=bi1
            count+=1
            arr2[i]=bi2
            count+=1
            print(arr1,'      ', arr2)
            i+=1
        m+=1
        if(n-m >= 0):
            i= 0
        else:
            i = -1
            bi1 = binary_convert(bi1)
            bi2 = binary_convert(bi2)
        bi1 = binary_convert(bi1)
        bi2 = binary_convert(bi2)
                
               
                        
            
            
    return count





        
    
    
    
