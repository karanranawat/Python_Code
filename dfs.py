'''
Depth first search algorithm

'''

class Graph(object):
# Undirected Graph
    nodes_dict = {}
    
    def __init__(self, size,node_list):
        self.size = size
        for i in node_list:
            self.nodes_dict[i] = [] #initialize empty list

    def get(self):
        return self.nodes_dict

    def print_adj_list(self):        
        for d in self.nodes_dict:
            print '<%d>' % d
            print self.nodes_dict[d]

    def add_edge(self,a,b):
#         for i in self.nodes_dict[a]:
#             self.nodes_dict[i].append(b)
#           
#         self.nodes_dict[a].append(b)
# 
#         for i in self.nodes_dict[b]:
#             self.nodes_dict[i].append(a)
#       
#         self.nodes_dict[b].append(a)
      self.nodes_dict[a].append(b)
      self.nodes_dict[b].append(a)  


def dfs(graph,fr):

    dict = graph.get()

    marked = {}
    for d in dict:
      marked[d] = 0
    
    stack = [fr]
    
  #   print 'initial stack: '
#     print stack
#         
    while stack:
      vertex = stack.pop()
#       print 'popped vertex = %d' % vertex
      if marked[vertex] == 0:
        marked[vertex] = 1
        stack.extend(dict[vertex])


    for d in marked:
        if marked[d]==0:
            print 'Not Connected'
            return
    print 'Connected'
    

if __name__ == '__main__':
    n = 4 # size of graph
    node_list = [1,2,3,4]
    graph = Graph(n, node_list)
    
    graph.add_edge(1,3)
    graph.add_edge(1,2)
    graph.add_edge(3,4)

    graph.print_adj_list()

    dfs(graph,4)
