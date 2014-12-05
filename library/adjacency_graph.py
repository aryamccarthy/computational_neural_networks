import networkx as nx

def MakeAdjacencyGraph(n, type, freq=0.5, wexc=0.1):
  G = nx.DiGraph()
  G.add_nodes_from(xrange(0,n))

  for i in xrange(0,n):
    for j in xrange(i+1, n):
      G.add_edge(i,j,weight=wexc)
      G.add_edge(j,i,weight=wexc)
  return G