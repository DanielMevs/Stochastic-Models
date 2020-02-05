import sys
sys.path.insert(0, '/home/daniel/Stochastics/helper_functions/')

import points as pt

'How many functions defined on n points are possible if each functional value is either 0 or 1?'

ans = 'y'
aList = []
n = 0


while ans == 'y' or ans == 'Y':
    n = int(input('Enter a value for n: '))
    aList = pt.populate(n)
    print('Your points: ', aList)
    aList = pt.binarify(aList)
    print('f(i) for points i=1 to i=n: ', aList)
    print('\nThe above is used to illustrate just one way to get the values for f(i). '
          'However for the total values we must use the equation 2^n; in our case: ', n*n)
    ans = input('Would you like to test another value of n?(y or n): ')
    
