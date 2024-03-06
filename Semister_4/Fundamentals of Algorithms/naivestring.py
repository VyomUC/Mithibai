def find(string, pattern):
    if len(string) < len(pattern):
        return "Match not found"
    for i in range(len(string) - len(pattern) + 1):
        if string[i:i+len(pattern)] == pattern:
            return f"Match found at index {i}"
    return "Match not found"

string = "abcdabce"
pattern = "bce"
print(find(string, pattern))