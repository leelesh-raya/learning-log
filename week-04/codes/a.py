import numpy as np

# Consider two random arrays A and B, check if they are equal (★★☆)


import numpy as np

false=0
true=0
while True:
    a = np.random.randint(0,2,4)
    b = np.random.randint(0,2,4)
    if np.array_equal(a,b) is True:
        true+=1
    else:   
        false += 1
    if true==10:
        break

print(false/true)

