import sys
sys.path.insert(0, '/home/daniel/Stochastics/helper_functions/')

from combinations import combine
#from permutations import permute
from cartesian import product


'''A college planning committee consists of 3 freshmen, 4 sophmores, 5 juniors,
and 2 seniors. A subcommittee of 4, consisting of 1 person from each class, is
to be chosen. How many different subcommittees are possible?'''

possibleFreshmenChosen = combine(3,1)
possibleSophmoresChosen = combine(4,1)
possibleJuniorsChosen = combine(5,1)
possibleSeniorsChosen = combine(2,1)
possibleCommittees = product([possibleFreshmenChosen, possibleSophmoresChosen,
                              possibleJuniorsChosen, possibleSeniorsChosen])

print('Ways to choose 1 freshman out of 3: ', possibleFreshmenChosen)
print('Ways to choose 1 sophmore out of 4: ', possibleSophmoresChosen)
print('Ways to choose 1 junior out of 5: ', possibleJuniorsChosen)
print('Ways to choose 1 senior out of 2: ', possibleSeniorsChosen)
print('\nThe cardinality of the cartesian product, or the number of all '  
    'ordered pairs between elements from the set of 4 classes ', possibleCommittees)







