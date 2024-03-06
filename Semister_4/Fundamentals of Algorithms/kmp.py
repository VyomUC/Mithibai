def kmp(string, pattern, lps):
    if len(string) < len(pattern):
        return "Invalid"

    i, j = 0, 0
    while i < len(string):
        if string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == len(pattern):
            return f"Found at index: {i-j}"
    return "Not found"

def findLPS(pattern):
    lps = [0]*len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps

string = "abc abcdab abcdabcdabde"
pattern = "abcdabd"
lps = findLPS(pattern)
print(kmp(string, pattern, lps))