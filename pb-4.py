# Multiply two matrices using recursion.

def matrix_multiply(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    
    result = [[0 for _ in range(p)] for _ in range(m)]
    
    def compute_element(i, j, k=0):
        if k == n:
            return 0
        return A[i][k] * B[k][j] + compute_element(i, j, k + 1)
    
    def fill_matrix(i, j):
        if i == m:
            return
        if j == p:
            fill_matrix(i + 1, 0)
            return
        result[i][j] = compute_element(i, j)
        fill_matrix(i, j + 1)
    
    fill_matrix(0, 0)
    return result

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = matrix_multiply(A, B)

for row in result:
    print(row)
