from nose.tools import *
import library
import library.adjacency_graph
import library.ode


# The package nosetests is required to perform
# testing; go to the project root and run
# nosetests -s (which gives printed output).


def setup():
  print "SETUP!"


def teardown():
  print "TEAR DOWN!"


def test_basic():
  print "I RAN!"


class TestODE(object):
  """docstring for TestODE"""

  def test_ODE_stuff(self):
    integrator = library.ode.Euler_Integrator(lambda x,y,params: x**2)
    xnext = integrator.step(0, 0, 1)
    print xnext

class TestAdjacencyMake(object):
  """docstring for AdjacencyMakeTest"""

  @classmethod
  def setup_class(cls):
    print "Class setup goes here."

  @classmethod 
  def teardown_class(cls):
    print "Class teardown goes here."

  def test_making_graph(self):
    NN = 20

    # set up timestepping
    time_initial = 0
    time_final = 20 * (NN**2)
    dt = 0.01

    # Scale coupling strength with number of cells.
    wexc = 0.2 / NN

    cgraph = library.adjacency_graph.MakeAdjacencyGraph(NN, "all", 0, wexc)
    print cgraph