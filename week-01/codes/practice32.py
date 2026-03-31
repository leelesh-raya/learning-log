spam=[
 
]



def rotatemat(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()        
    

    

    
                       

rotatemat(spam)
print(spam)



#Corrections: Initially used complex indexing and extra space, violating the in-place constraint. 
# Learned that rotation can be done cleanly by transposing the matrix and reversing each row, simplifying the logic.
