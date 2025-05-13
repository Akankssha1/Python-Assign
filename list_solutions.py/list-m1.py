def generate_matrix(n,m):
    matrix=[[i*j for j in range(m)] for i in range(n)]
    return matrix
print(generate_matrix(3,3))