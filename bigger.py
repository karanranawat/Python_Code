# Most efficient algorithm to implement this logic
# Dont use in-built functions
# The in-built itertools funciton calculates all the permutations
#Find the highest index i such that s[i] < s[i+1]. If no such index exists, the permutation is the last permutation.
#Find the highest index j > i such that s[j] > s[i]. Such a j must exist, since i+1 is such an index.
#Swap s[i] with s[j].
#Reverse all the order of all of the elements after index i


import itertools

def find_next(string):
    if len(string) == 1:
      return string
    str1 = sorted(string)
    perm = itertools.permutations(str1)
    found = 0
    for p in perm:
        join_string = ''.join(p)
        if join_string == string:
          break
    return ''.join(perm.next()) #return next lexographical ordering
          
      
    
N = input() #nnumber of test cases

for i in range(N):
  str1 = raw_input()
  next_big = find_next(str1)
  if next_big == str1:
    print 'no answer'
  else:
    print next_big