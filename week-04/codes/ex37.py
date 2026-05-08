# How to ignore all numpy warnings (not recommended)? (★☆☆)


import numpy as np

# Suicide mode 
defaults = np.seterr(all='ignore')
print(np.ones(1) /0)

# Back to sanity
_ = np.seterr(**defaults)
print(np.ones(1) /0)

# with a context manager
with np.errstate(all='ignore'):
    print(np.ones(1)/0)

# seterr options
np.seterr(all="ignore")    # silence everything
np.seterr(all="warn")      # warn (default)
np.seterr(all="raise")     # raise exception instead of warning
np.seterr(all="print")     # print to terminal
np.seterr(divide="ignore", invalid="warn")  # per-operation control

# The operation types
np.seterr(
    divide="ignore",    # division by zero — 1/0, produces inf
    invalid="ignore",   # invalid operation — 0/0, produces nan
    overflow="ignore",  # result too large for dtype — produces inf
    under="ignore"      # result too small for dtype — rounds to 0
)