'''
Union, find and connected operations take linear time
Count operations takes constant time
'''
class WeightedQuickUnion(object):

    # Constructor
    def __init__(self, N):
        self.count = N
        self.id = range(0,N)
        self.sz = range(0,N)
        for i in range(0,N):
          self.id[i] = i
          self.sz[i] = 1

    # Slow Union method
    def union(self,p,q):
      i = self.find(p)
      j = self.find(q)
      if i == j:
        return  # already connected

      if self.sz[i] < self.sz[j]:
          self.id[i] = j
          self.sz[j] += self.sz[i]
      else:
          self.id[j] = i
          self.sz[i] += self.sz[j]
          
      self.count -= 1
      

    # Quick Find
    def connected(self,p,q):
      return self.find(p) == self.find(q)
    

    # Returns total count of number of component in the graph
    def total_count(self):
      return self.count
    
    # Validate if p is a valid index
    def validate(self, p):
      N = len(self.parent)
      if p<0 or p>=N:
        raise Exception('Index ' + p + ' is  not between 0 and ' + N)
    
    # Returns the root of the tree
    def find(self,p):
      while p != self.id[p]:
        p = self.id[p]
      return p
    
    # Check if two components are connected  
    def connected(self, p, q):
      return self.find(p) == self.find(q)
    

if __name__ == '__main__':
#     f = open('tinyUF.txt')
    f = open('mediumUF.txt')
    N = int(f.readline())
    
    uf = WeightedQuickUnion(N)

    for line in f:
      l = line.split()
      p = int(l[0])
      q = int(l[1])
      if uf.connected(p,q):
        continue
      else:
        uf.union(p,q)
        print '%d - %d' % (p,q)
      
    print 'Total count %d' % uf.total_count()
