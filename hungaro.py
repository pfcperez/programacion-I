# http://software.clapper.org/munkres/, http://software.clapper.org/munkres/
#https://www.youtube.com/watch?v=VDos3cM9Rh0
from munkres import Munkres, print_matrix

matrix = [[13, 7,2,1],[5,18,8,6],[8,3,11,15],[4,2,5,3]]

m = Munkres()

indexes = m.compute(matrix)
print(matrix, 'El menor costo de la matriz')
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total+=value
    print(row,column,'-> ', value)
print('El costo total es ', total)



