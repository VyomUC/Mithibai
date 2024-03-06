def determinant(m):
    # Calculating determinant of a 3x3 matrix directly
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
            m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
            m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

def minor(m, i, j):
    # Constructing a submatrix for minor calculation and then calculating its determinant
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def determinant_2x2(m):
    # Determinant of a 2x2 submatrix
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def cofactor(m):
    cof = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            sign = (-1) ** (i + j)
            sub_minor = minor(m, i, j)
            cof[i][j] = sign * determinant_2x2(sub_minor)
    return cof

def transpose(m):
    return [list(i) for i in zip(*m)]

def inverse(m):
    det = determinant(m)
    if det == 0:
        raise ValueError("Matrix is singular, cannot find its inverse.")
    cof = cofactor(m)
    adj = transpose(cof)
    return [[adj[i][j] / det for j in range(3)] for i in range(3)]

def multiply(mat1, mat2):
    result = [[sum(a*b for a, b in zip(row, col)) for col in zip(*mat2)] for row in mat1]
    return result

def changebasis(vector, oldbasis, newbasis):
    inv_oldbasis = inverse(oldbasis)
    transform_matrix = multiply(newbasis, inv_oldbasis)
    vector_column = [[v] for v in vector]  # Make sure vector is in column format for multiplication
    result = multiply(transform_matrix, vector_column)
    return [val[0] for val in result]  # Convert result back to 1D list

# Example use
m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # Identity matrix (old basis)
m2 = [[1, 3, 4], [2, -1, 1], [1, 0, 2]]  # New basis
vector = [2, 3, -1]

# Applying change of basis
print(changebasis(vector, m1, m2))