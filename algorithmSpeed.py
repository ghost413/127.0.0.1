import matplotlib.mlab as mlab
from time import time

# gets start time
start = time

# put code to be timed here


# gets end time
end = time

# gets total time in seconds
total_time = end - start

# converts to microseconds
total_time *= 1000000

print("Execution time:", total_time, "us")
