class Error(Exception):
    pass

class kTooBig(Error):
    pass

def permute(n, k):
    try:
        if(k > n):
            raise kTooBig()

        if(k == 0):
            return int(1)
        
        else:
            return int(n * permute(n-1, k-1))
        
    except kTooBig:
        print("Invalid parameters, k must be bigger than n\n")
    

#print(permute(4,3))
