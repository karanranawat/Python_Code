from WeightedQuickUnion import WeightedQuickUnion

class Percolation(object):
  
  def __init__(self,N):
    self.grid_width = N
    self.no_of_elements = N*N+2
    
    self.is_open_list = [ False for x in range(0,self.no_of_elements) ]
    
    self.virtual_top_index = 0
    self.virtual_bottom_index = self.no_of_elements-1
    
    self.is_open_list[self.virtual_top_index] = True
    self.is_open_list[self.virtual_bottom_index] = True
    
    self.uf = WeightedQuickUnion(self.no_of_elements)
    
  def xy_to_index(self,row,col):
    return ((row-1)*self.grid_width + col)

  def connect_site_to_neighbor(self, site_index, row, col):
    neighbor_index = self.xy_to_index(row,col)
    self.uf.union(site_index, neighbor_index)
  
  def connect_element_to_open_neighs(self,row,col):
    self.site_index = self.xy_to_index(row,col)

    if row == 1:  # Connect top virtual site to current site
      self.uf.union(self.virtual_top_index,self.site_index)

    if row == self.grid_width: # Connect virtual bottom site to current site
      self.uf.union(self.virtual_bottom_index,self.site_index)

    if row != 1: #Above neighbor exists
      if self.is_open(row-1,col):
        self.connect_site_to_neighbor(self.site_index,row-1,col)

    if row != self.grid_width:  # Below neighbor exists
      if self.is_open(row+1,col):
        self.connect_site_to_neighbor(self.site_index,row+1,col)

    if col !=1: # Left neighbor exists
      if self.is_open(row,col-1):
        self.connect_site_to_neighbor(self.site_index,row,col-1)

    if col != self.grid_width: # Right  neighbor exists
      if self.is_open(row, col+1):
        self.connect_site_to_neighbor(self.site_index, row,col+1)
  
  def open(self,i,j):
    index = self.xy_to_index(i,j)
    #print 'index to open = %d' % index
    self.is_open_list[index] = True
    self.connect_element_to_open_neighs(i,j)
    
  def is_open(self,i,j):
    return self.is_open_list[self.xy_to_index(i,j)]
    
  def percolates(self):
    return self.uf.connected(self.virtual_top_index, self.virtual_bottom_index)
    
    

if __name__ == '__main__':
# Testing for instance of Percolation data type
  f = open('per_testing/input6.txt','rU')
  first_line = True
  for line in f:
    if first_line == True:
      N = int(line)
      print N
      p = Percolation(N)
      first_line = False
    else:
      line_list = line.split()
      if len(line_list) == 0:
        continue
      print line_list
      i = int(line_list[0])
      j = int(line_list[1])
      p.open(i,j)


  print p.percolates()
