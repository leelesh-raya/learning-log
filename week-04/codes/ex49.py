# Consider two random arrays A and B, check if they are equal (★★☆)


import numpy as np



a = np.random.randint(0,2,4)
b = np.random.randint(0,2,4)


# WITHOUT TOLERANCE
# Integers (whole array) 
print(np.array_equal(a,b)) 

# Integers (element-wise)
print(a==b)


# WITH TOLERANCE
# Floats (whole array)
print(np.allclose(a,b))

# Floats (element-wise)
print(np.isclose(a,b))


# |A - B| <= atol + rtol * |B|