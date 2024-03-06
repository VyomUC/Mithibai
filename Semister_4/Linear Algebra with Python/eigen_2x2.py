import math

def find_eigenvalues(a, b, c, d):
    trace = a + d
    determinant = a * d - b * c
    temp = math.sqrt(trace ** 2 - 4 * determinant)
    lambda1 = (trace + temp) / 2
    lambda2 = (trace - temp) / 2
    return [lambda1, lambda2]

def find_eigenvectors(a, b, c, d, eigenvalues):
    eigenvectors = []
    for lambda_val in eigenvalues:
        # For A - lambda*I, the matrix becomes:
        # [(a - lambda), b]
        # [c, (d - lambda)]
        # To find a non-trivial solution, we can set x = 1 (if possible), and solve for y,
        # or if b and c are both 0, we handle differently.
        if b == 0 and c == 0:
            eigenvectors.append([1, 0])  # or any non-zero vector if a - lambda = 0
        elif b != 0:
            # Equation becomes: (a - lambda)*x + b*y = 0
            # If we set x = 1, then y = -(a - lambda)/b
            y = -(a - lambda_val) / b
            eigenvectors.append([1, y])
        else:
            # If b is 0, but c is not, it means we can't directly solve for y in terms of x from the first row.
            # Instead, we look at the second row, or we can set y = 1 for simplicity, and solve for x if necessary.
            # This means x can be any value when c is not affecting the second equation significantly.
            # In practice, we might need to solve for x when c != 0, but for simplicity, let's set x when y = 1.
            x = -(d - lambda_val) / c
            eigenvectors.append([x, 1])
    return eigenvectors

def eigen_analysis(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    eigenvalues = find_eigenvalues(a, b, c, d)
    eigenvectors = find_eigenvectors(a, b, c, d, eigenvalues)
    print("Eigenvalues and Eigenvectors:")
    for i in range(len(eigenvalues)):
        print(f"Eigenvalue: {eigenvalues[i]}, Eigenvector: {eigenvectors[i]}")

# Example matrix
m = [[4, 2], [1, 3]]
eigen_analysis(m)
