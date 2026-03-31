'''Matrix Operations
Write a function that takes two matrices and returns their product. 
If multiplication is not possible, return 'Error: incompatible dimensions'.'''

a=[[1,2],
   [3,4]]
b=[[5,6],
   [7,8]]


def multrix(x,y):
    z=[]
    for i in range(len(x)):
        z.append([0]*len(y))
        for j in range(len(y[0])):
            for k in range(len(y)):
                z[i][j]+=x[i][k]*y[k][j]
                
        
        
    return z
print(multrix(a,b))

                                                                 
#This problem was solved after 'practice26.py'. Typed here to fill an empty file created by mistake.

# Correction: Tried to solve this problem intuitively but couldn't. The effort put in helped understand the logic behind the code.
# Pretended to intuitively solve this problem after understanding the logic.
