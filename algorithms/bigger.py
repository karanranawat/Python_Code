
# Problem : Find the next largest string according to lexographic ordering




# Find the next largest using python's itertools library
# The in-built itertools funciton calculates all the permutations
# The drawback of this implementation is that is calculates all possible
# permutations of a string
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


# The following algorithm finds the next largest lexographically larger string
# without the need to find all the permutations of a sring

# Steps:
# 1. Find the highest index i such that s[i] < s[i+1]. If no such index exists, the permutation is the last permutation.
# 2. Find the highest index j > i such that s[j] > s[i]. Such a j must exist, since i+1 is such an index.
# 3. Swap s[i] with s[j].
# 4. Reverse all the order of all of the elements after index i          
def find_next_native(string):
  if len(string)==1:
    return string
  
  #step 1. find highest index i such that s[i] < s[i+1] exists
  i = 0
  high_i = -1
  for i in range(0,len(string)-1):
    if string[i] < string[i+1]:
      high_i = i         
  
#   print 'high i=%s', (high_i)
  
  if high_i == -1:
    return string # no answer exists for this permuatation
  else:
    i = 0
    for j in range(high_i+1,len(string)):
      if string[j]>string[high_i]:
        high_j = j    
    
#     print 'high j=%s', (high_j)
    string_list = list(string)
    
#     print string_list
    
    tmp = string_list[high_j]
    string_list[high_j] = string_list[high_i]
    string_list[high_i] = tmp
    
#     print string_list
    
    last_part = string_list[high_i+1:]
    
#     print 'first part'
#     print string_list[:high_i]
#     print last_part
    
    return ''.join(string_list[:high_i+1] + last_part[::-1] )
    
N = input() #nnumber of test cases

for i in range(N):
  str1 = raw_input()
  next_big = find_next_native(str1)
  if next_big == str1:
    print 'no answer'
  else:
    print next_big