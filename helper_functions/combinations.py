class Error(Exception):
    pass

class kTooBig(Error):
    pass

def combine(n, k):
    
    try:
        if(k > n):
            raise kTooBig()
        
        if(k == 0):
            return int(1)
        
        else:
            return int(n * (combine(n-1, k-1))/k)
        
    except kTooBig:
        print("Invalid parameters, k must be bigger than n\n")

    

#print(combine(22,22))
