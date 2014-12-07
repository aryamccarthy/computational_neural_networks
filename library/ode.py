import abc

class Integrator(object):
  """docstring for Integrator"""

  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def step(self, tn, xn, dt, params=None):
    pass


class Euler_Integrator(Integrator):
  """docstring for Euler_Integrator"""
  def __init__(self, func):
    super(Euler_Integrator, self).__init__()
    self.function = func
    
  def step(self, t, x, dt, params=None):
    K1 = self.function(t, x, params)
    
    x_next = x + dt * K1
    return x_next


class RK2_Integrator(Integrator):
  """docstring for Runge_Kutta_2_Integrator"""
  def __init__(self, func):
    super(RK2_Integrator, self).__init__()
    self.function = func
  
  def step(self, t, x, dt, params=None):
    K1 = self.function(t, x, params)
    K2 = self.function(t+dt, x+(dt*K1), params)

    x_next = x + dt * (K1 + K2)/2
    return x_next


class RK4_Integrator(Integrator):
  """docstring for RK4_Integrator"""
  def __init__(self, func):
    super(RK4_Integrator, self).__init__()
    self.function = func
    
  def step(self, t, x, dt, params=None):
    k1 = self.function(t, x,  params)
    k2 = self.function(t + dt/2.0, x + k1*dt/2.0, params)
    k3 = self.function(t + dt/2.0, x + k2*dt/2.0, params)
    k4 = self.function(t + dt, x + k3*dt, params)

    x_next = x + dt*(k1 + 2*k2 + 2*k3 + k4)/6
    return x_next


def vector_with_step_size(start, end, step_size):
  """
  From documentation on np.arange: 
  When using a non-integer step, such as 0.1, the results will often not 
  be consistent. It is better to use linspace for these cases.

  That's why we're wrapping np.linspace to take the args for np.arange.
  """
  num_intervals = int(np.round((end-start)/step_size))
  return np.linspace(start, end, num_intervals + 1)


def simple_object_timestepper(integrator, xI, tI, tF, dt):
  # Establish dimensions of the ODE system.
  dim = len(xI)

  # Time vector
  t = vector_with_step_size(tI, tF, dt)

  # Initialize storage.
  x = np.empty((len(t), dim))
  # coeff_list = []
  x[0,:] = xI

  # Run the solver.
  for n in xrange(len(t)):
    x_next = integrator.step(t[n], x[n,:], dt)
    x[n+1, :] = x_next # Update next column of entries

  return t, x

