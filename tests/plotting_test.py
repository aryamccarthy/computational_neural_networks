import library.nnlib as nnlib
import library.graph as graph

import numpy as np

def setUp():
  print "Hello"

def tearDown():
  print "Goodbye"

def test_plotting():
  NN = 20 # number of neurons

  # set up time intervals
  ti = 0.0
  tf = 10.0
  dt = 0.01

  #TODO: finish me

  # generate feed-forward spikes
  density = 5.0
  ff_neurons = nnlib.generate_feed_forward_spikes(NN, ti, tf-ti, density)
  print ff_neurons

  # set up network and initial conditions
  cgraph = graph.random_digraph(NN, 2, weight=0.1)
  IC = np.zeros((NN, 2))
  IC[:,0] = np.random.rand(NN)
  IC[:,1] = np.zeros(NN)

  # set up reference integrators

  # do the simulations

  # show some plots

