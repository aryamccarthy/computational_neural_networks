from __future__ import absolute_import, print_function
from library import graph
import sys

def main():
  NN = 20 # Number of neurons

  # # set up timestepping
  # ti = 0
  # tf = 20 * (NN**2)
  # dt = 0.01

  # Scale coupling strength with number of neurons
  wexc = 0.2/NN

  # Set up network and initial conditions
  # "freq" is an unused argument; set to 0 here.
  cgraph = graph.MakeAdjacencyGraph(NN, "all", 0, wexc)
  print(cgraph, file=sys.stderr)

if __name__ == '__main__':
  main()