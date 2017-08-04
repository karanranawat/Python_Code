def no_of_anagrams(string):
  
  # Get all possibles substring of length > 1 and length < size of string
  count = 0
  for size in range(1,len(string)):
    for i in range(0,len(string)-size+1):      
#       print 'key-->%s' % string[i:i+size]
      for j in range(i+1,len(string)-size+1):
       #  slice = ''.join(sorted(string[i:i+size]))
#         print slice
#         if slice in dict:
#           dict[slice] += 1
#           print 'Increased count'
#         else:
#           dict[slice] = 0
#         print string[j:j+size]
        if sorted(string[i:i+size])==sorted(string[j:j+size]):
          count += 1
    
#     for d in dict:
#       if dict[d]>0:
#         count += dict[d]
  return count

def main():
  N = input()
  for i in range(0,N):
    string = raw_input()
    print no_of_anagrams(string)
    # this 

if __name__ == '__main__':
  main()
