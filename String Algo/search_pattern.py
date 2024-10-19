def search_pattern(text, pattern):
    m = len(pattern)
    n = len(text)
    print(n - m +1)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j +=1
        if j == m:
            print(f"Pattern found at {i}")

print(search_pattern("AABACAADAABAABA","AABA"))