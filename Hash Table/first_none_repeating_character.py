def noneRepeatingChar(s:str):
    table = {}
    for c in s:
        if c in table:
            table[c] += 1
        else:
            table[c] = 1
    for c in s:
        if table[c] == 1:
            return c 
        
print(noneRepeatingChar("abzddab"))