import random
# imported for random generation; I hope this goes away soon.

def generate_feed_forward_spikes(num_neurons, time, dt, density):
  """
  Generate a list of num_neurons lists of random spikes, with supplied 
  density.
  """
  neurons = [[]]*num_neurons # a list of num_neurons lists

  for spikes in neurons: # spikes is a list
    ff_spike_time = time
    while True:
      dt_spike = 2.0 * random.random() / density
      ff_spike_time += dt_spike
      if ff_spike_time > time + dt:
        break
      ff_spike_weight = random.random() / 10.0
      spikes.append((ff_spike_time, ff_spike_weight))
  return neurons