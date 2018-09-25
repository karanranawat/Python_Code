class Vertex(object):
  def __init__(self,key):
    self.id = key
    self.connectedTo = {}

  def addNeighbor(self, nbr, weight=0):
    self.connectedTo[nbr] = weight

  def getConnections(self):
    return self.connectedTo.keys()

  def getId(self):
    return self.id

  def getWeight(self,nbr):
    return self.connectedTo[nbr]


class Graph(object):
  def __init__(self):
    self.vertList = {}
    self.numVertices = 0

  def addVertex(self,key):
    self.numVertices += 1
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex

  def __contains__(self,n):
    return n in self.vertList

  def addEdge(self, f, t, cost=0):
    if f not in self.vertList:
      nv = self.addVertex(f)
    if t not in self.vertList:
      nv = self.addVertex(t)

    self.vertList[f].addNeighbor(self.vertList[t],cost)

  def getVertices(self):
    return self.vertList.keys()

  def __iter__(self):
    return iter(self.vertList.values())

def bfs(g,vertex,N):
  import Queue as queue
  distance = {}
  visited = []
  
  vq = queue.Queue()
  vq.put(g.vertList[vertex])
  visited.append(vertex)
  distance[g.vertList[vertex].getId()] = 0

  level_sum = 0
  while vq.empty() == False:
    v = vq.get()    
    for ct in v.connectedTo:      
      if ct.getId() not in visited:
        vq.put(ct)
        visited.append(ct.getId())
        distance[ct.getId()] = distance[v.getId()] + v.getWeight(ct)
    
  for i in range(1,N+1):
    if vertex == i:
      continue    
    if i not in distance:
      print '-1',
    else:
      print distance[i],
  print ''

if __name__ == '__main__':
  T = input() # no of test cases

  for i in range(T):
    input_line = raw_input()
    input_list = input_line.split()
    input_list = map(int,input_list)

    N = input_list[0] #number of nodes
    M = input_list[1] #edges
    
    g = Graph() # create new graph
    
    for j in range(1,N+1):
      g.addVertex(j)

    for j in range(M):
      input_line = raw_input()
      input_list = input_line.split()
      input_list = map(int,input_list)
      g.addEdge(input_list[0], input_list[1], 6)
      g.addEdge(input_list[1], input_list[0], 6)

    source_vertex = input()    
    bfs(g,source_vertex,N)

  
  
  
