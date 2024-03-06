def check(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def find(string, pattern):
    if len(string) < len(pattern):
        return "Match not found"
    
    psum = sum([ord(char) - 96 for char in pattern])
    csum = sum([ord(char) - 96 for char in string[:len(pattern)]])

    for i in range(0, len(string) - len(pattern) + 1):
        if i != 0:
            csum = csum - (ord(string[i-1]) - 96) + (ord(string[i+len(pattern)-1]) - 96)
        
        if csum == psum:
            if check(string[i: i + len(pattern)], pattern):
                return f"Match found at index {i}"
    return "Match not found"

string = "ccaccaaedba"
pattern = "dba"
print(find(string, pattern))
