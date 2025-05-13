def transpose_matrix(matrix):
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed_matrix
matrix=([1,2,3],
        [4,5,6])
print(transpose_matrix(matrix))
