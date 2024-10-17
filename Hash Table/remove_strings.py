def removeString(s:str, k:str):
    temp = ''
    table = {}
    for c in s:
        if c == k:
            continue
        else:
            temp = temp + c
    return temp

print(removeString("careermonk",'e'))