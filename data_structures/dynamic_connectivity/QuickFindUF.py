class QuickFindUF(object):
    # Constructor
    def __init__(self, N):
        self.count = N
        self.id = range(0,N)
        for i in range(0,N):
          self.id[i] = i

    # Slow Union method
    def union(self,p,q):
      pid = self.id[p]
      qid = self.id[q]

      for i in range(0,len(self.id)):
        if self.id[i]==pid: 
          self.id[i] = qid
      self.count -= 1

    # Quick Find
    def connected(self,p,q):
      if self.id[p] == self.id[q]: 
        return 1
      else:
        return 0

    def total_count(self):
      return self.count
      
    def validate(self, p):
      N = len(self.id)
      if p<0 or p>=N:
        raise Exception('Index ' + p + ' is  not between 0 and ' + N)
    
    def find(self,p):
      validate(p)
      return self.id[p]
      
    def connected(self, p, q):
      self.validate(p)
      self.validate(q)
      return self.id[p] == self.id[q]
    

if __name__ == '__main__':
    f = open('largeUF.txt')
    N = int(f.readline())
    
    uf = QuickFindUF(N)

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