'''Nested Lists
Write a function that takes a matrix (list of lists) and returns its transpose 
— rows become columns, columns become rows. Do not use any libraries.
'''

spam=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]


def transpose(matrix):
    eggs=[]
    for i in range(len(matrix[0])):
        cheese=[]
        for j in range(len(matrix)):
            cheese.append(matrix[j][i])
        eggs.append(cheese)
    return eggs

print(transpose(spam))