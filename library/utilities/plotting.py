import matplotlib.pyplot as plt

def plot_detailed_VG(t, VG, rcolls, neur_nums):
  pass

def plot_V_vs_t_all(t, VG):
  """Plot all voltage traces on a single plot.
  :param t: times
  :param VG: 3D matrix
  :return none
  """
  plt.plot(t, VG[:,:,0])

def plot_g_vs_t_all(t, VG):
  """Plot all conductance traces on a single plot.
  :param t: times
  :param VG: 3D matrix
  :return none
  """
  plt.plot(t, VG[:,:,1:])

def plot_VG_vs_t_all_subplot(t, VG, Nsub):
  """Plot the V and G for the first Nsub neurons.

  :param t: list of times, the independent variable of the plot.
  :param VG: 3D matrix indexed VG[time][neuron][attribute_id]
  Voltage must be the first attribute; the rest are conductances.
  :param Nsub: Number of neurons to test
  :return none
  """
  try:
    neurons_to_plot = xrange(Nsub)
  except TypeError:
    neurons_to_plot = Nsub

  for (i, neuron) in enumerate(neurons_to_plot):
    plt.subplot(len(neurons_to_plot), 1, i+1)
    # Voltage
    plt.plot(t, VG[:,neuron,0], linewidth=2.0, label='voltage')
    # conductances
    plt.plot(t, VG[:,neuron,1:], linewidth=2.0, label='conductance')