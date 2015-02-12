import matplotlib.pyplot as plt
import numpy as np
from library.utilities import plotting as luplot

def main():
  times = xrange(10)
  data = [[(x, x+1, x+2, x+3)]*7 for x in xrange(10)]
  plot(times, data)

def plot(times, xvals):
  plt.figure(1)
  plt.title('Voltage and Conductance for selected neurons')
  luplot.plot_VG_vs_t_all_subplot(times, np.array(xvals), 3)
  for i in xrange(1,4):
    plt.subplot(3, 1, i)
    plt.legend(loc=2)
  plt.xlabel('time')
  plt.show()

if __name__ == '__main__':
  main()