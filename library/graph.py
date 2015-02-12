import networkx as nx
import numpy as np

def MakeAdjacencyGraph(n, type, freq=0.5, wexc=0.1):
  '''Temporary implementation that only generates complete graph.'''
  G = nx.complete_graph(n, nx.DiGraph())
  # Should profile this.
  for edge in G.edges_iter():
    nx.set_edge_attributes(G, 'weight', {edge: wexc})
  nx.freeze(G) # To prevent unintended modification of G's structure
  return G
#

