# how to read the following file? (★★☆)

'''     1, 2, 3, 4, 5
        6,  ,  , 7, 8
         ,  , 9,10,11       '''

import numpy as np
from io import StringIO

fake_file = StringIO('''     1, 2, 3, 4, 5
        6,  ,, 7, 8
                     
         ,  , 9,10,11       ''')

z = np.genfromtxt(fake_file, delimiter=',', dtype='int', filling_values = 0)
print(z)


# StringIO: Simulates a physical file in RAM for easy testing.
# genfromtxt: Robust reader that handles missing values and delimiters.
# filling_values: Replaces empty gaps with 0 to prevent code crashes.