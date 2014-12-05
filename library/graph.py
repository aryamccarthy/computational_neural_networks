import networkx as nx
import numpy as np

def MakeAdjacencyGraph(n, type, freq=0.5, wexc=0.1):
  G = nx.DiGraph()
  G.add_nodes_from(xrange(n))

  for i in xrange(n):
    for j in xrange(i):
      G.add_edge(i,j,weight=wexc)
      G.add_edge(j,i,weight=wexc)
  return G

def random_digraph(num_neurons, neighbors, weight=0.1):
  G = nx.MultiDiGraph()
  G.add_nodes_from(xrange(num_neurons))

  for i in xrange(num_neurons):
    somerand = num_neurons * np.random.rand(neighbors)
    neighs = np.unique(np.floor(somerand))
    for j in neighs:
      G.add_edge(i, int(j), weight=weight)
  return G