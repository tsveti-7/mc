import constants as const
import sys, getopt
import numpy as np
import time
import math

def main(argv):
  num_e = 1000

  try:
    opts, args = getopt.getopt(argv,"h:n:",["num_e="])
  except getopt.GetoptError:
    print('drift.py -n <number of electrons> [default: {}]'.format(num_e))
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      print('drift.py -n <number of electrons> [default: {}]'.format(num_e))
      sys.exit()
    elif opt in ("-n", "--number_of_electrons"):
      num_it = int(arg)

  print('Here we go ...')
  # Calculate the nucleus mass
  xmassn = const.n * const.xmassp
  # Initialize the accesleration variables in x, y direction
  acx = 0.0
  acy = 0.0
  # Initialize drift velocity
  vdrift = 0.0
  norm = 0

  # Initialize the random number generator with seed from current datetime
  # in case u want to debug the sript please comment the line below
  np.random.seed(seed=int(time.time()))
  for i in xrange(1, num_e):
    x = 0.0
    y = 0.0
    z = 0.0
    ttotal = 0.0
    vx = 0.0
    vy = 0.0
    vz = 0.0

    while z < const.zend:
      # Dummy line
      z += 0.1
      # Dummy line
      ttotal += 0.01
      # Implement actual logic

    vdrift += z/ttotal
    norm += 1

  print('Done')

if __name__ == "__main__":
  main(sys.argv[1:])
