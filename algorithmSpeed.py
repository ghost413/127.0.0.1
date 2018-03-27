import matplotlib.mlab as mlab
import numpy as np
from time import time
import math

a = [3.5, 5, 0]
b = [6, 1.3, 10]

# gets start time
start = time()

# put code to be timed here
# dist = mlab.dist(a[0], b[0])
# dist = np.sqrt(np.sum((a[0] - b[0]) ** 2))
# dist = np.sqrt(np.power(a[0] - b[0], 2) + np.power(a[1] - b[1], 2))
# dist = np.linalg.norm(a - b)
# dist = math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))

# gets end time
end = time()

# gets total time in seconds
total_time = end - start

# converts to microseconds
total_time *= 1000000

print("Execution time:", total_time, "us")
