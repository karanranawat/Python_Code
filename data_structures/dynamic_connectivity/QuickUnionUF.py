'''
Union, find and connected operations take linear time
Count operations takes constant time
'''
class QuickUnionUF(object):

    # Constructor
    def __init__(self, N):
        self.count = N
        self.parent = range(0,N)
        for i in range(0,N):
          self.parent[i] = i

    # Slow Union method
    def union(self,p,q):
      root_p = self.find(p)
      root_q = self.find(q)
      if root_p == root_q:
        return  # already connected
      
      self.parent[root_p] = root_q
      self.count -= 1
      

    # Quick Find
    def connected(self,p,q):
      if self.id[p] == self.id[q]: 
        return 1
      else:
        return 0

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
      self.validate(p)
      while p!=self.parent[p]:
        p = self.parent[p]
      return p
    
    # Check if two components are connected  
    def connected(self, p, q):
      return self.find(p) == self.find(q)
    

if __name__ == '__main__':
#     f = open('tinyUF.txt')
    f = open('mediumUF.txt')
    N = int(f.readline())
    
    uf = QuickUnionUF(N)

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