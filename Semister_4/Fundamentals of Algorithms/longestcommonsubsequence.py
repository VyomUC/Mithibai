def lcs(string1, string2):
    table = [[0 for _ in range(len(string1) + 1)] for _ in range(len(string2) + 1)]

    # Populate table
    for i in range(1, len(string2) + 1):
        for j in range(1, len(string1) + 1):
            if string2[i - 1] == string1[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    # Print table header
    print(end=' \t')
    for char in string1:
        print(char, end='\t')
    print()

    # Print table rows
    for i in range(1, len(string2) + 1):
        print(string2[i - 1], end='\t')
        for j in range(1, len(string1) + 1):
            print(table[i][j], end='\t')
        print()

    # Backtracking to find the LCS
    i, j = len(string2), len(string1)
    result = []
    while i > 0 and j > 0:
        if string2[i - 1] == string1[j - 1]:
            result.append(string2[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the result since we've built it backwards
    return ''.join(reversed(result))

print(lcs("LONGEST", "STONE"))
#print(lcs("execution", "intention"))