import sys
sys.path.insert(0, '/home/daniel/Stochastics/helper_functions/')

#from combinations import combine
#from permutations import permute
from cartesian import product

'''How many different 7-place license plates are possible if the first 3 places are to be
occupied by letters and the final 4 by numbers?'''

possibleLetters = cartesian([26, 26, 26])
possibleNumbers = cartesian([10, 10, 10, 10])
possiblePlates = cartesian([possibleLetters, possibleNumbers])

print('Ways to choose 3 letters from the English alphabet where '
      'the letters are replaceable = 26^3 = ', possibleLetters)
print('Ways to choose 4 numbers from the conventional base 10 number'
      ' system = 10^4 = ', possibleNumbers)
print('\nThe cardinality of the cartesian product, or the number of all '  
    'ordered pairs between elements from the set of'
    ' possibleLetters and  possibleNumbers: ', possiblePlates)
