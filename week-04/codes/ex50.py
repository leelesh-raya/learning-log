# Make an array immutable (read-only) (★★☆)

import numpy as np

arr = np.array([1, 2, 3, 4])
arr.flags.writeable = False

arr[0] = 1
print(arr)



print(arr.flags)

# C_CONTIGUOUS : True      — stored in row-major order
# F_CONTIGUOUS : True      — stored in column-major order
# OWNDATA : True           — owns its data
# WRITEABLE : True         — can be modified
# ALIGNED : True           — properly aligned in memory
# WRITEBACKIFCOPY : False  — no copy to write back