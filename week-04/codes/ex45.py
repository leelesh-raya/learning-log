# Consider a generator function that generates 10 integers and use it to build an array (★☆☆)

import numpy as np

def generator():
    for x in range (10):
        yield x

g = generator()
arr = np.fromiter(g, dtype= float, count=-1)
print(arr)


# - fromiter pulls computed values directly into an array — avoids intermediate list, halves peak memory usage