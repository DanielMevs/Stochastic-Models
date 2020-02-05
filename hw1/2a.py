import sys
sys.path.insert(0, '/home/daniel/Stochastics/helper_functions/')

from combinations import combine
#from permutations import permute
from cartesian import product

'''A small community conssits of 10 women, each of whom has 3 children.
If one woman and one of her children are to be chosen as mother and chid
of the year, how many different choices are possible?'''

possibleWomenChosen = combine(10,1)
possibleChildrenChosen = combine(3,1)
possiblePairs =  product([possibleWomenChosen, possibleChildrenChosen])


print('Ways to choose 1 woman out of 10: ', possibleWomenChosen)
print('Ways to 1 child out of 3: ', possibleChildrenChosen)
print('\nThe cardinality of the cartesian product, or the number of all '  
    'ordered pairs between elements from the set possibleWomenChosen and elements of the '
    'set possibleChildrenChosen : ', possiblePairs )







