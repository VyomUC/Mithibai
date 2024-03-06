def userinput(rows, cols):
    arr = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = int(input(f"Enter no. for row {i+1}, col {j+1}: "))
    print()
    return arr

def multiply(arr1, arr2):
    if len(arr1[0]) != len(arr2):
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")

    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result

print("Matrix 1")
r1 = int(input("Enter no. of rows: "))
c1 = int(input("Enter no. of cols: "))
arr1 = userinput(r1, c1)

print("Matrix 2")
r2 = c1  # Must match the number of columns in the first matrix for multiplication
c2 = int(input("Enter no. of cols for the second matrix: "))
arr2 = userinput(r2, c2)

prod = multiply(arr1, arr2)
print("Product of the two matrices:")
for row in prod:
    print(row)