import collections


def smallWindow(inputs, chars):
    assert chars != ''
    hashMap = collections.defaultdict(int)

    nneg = [0]
    def incr(c):
        hashMap[c] += 1
        if hashMap[c] == 0:
            nneg[0] -= 1
    def desc(c):
        if hashMap[c] == 0:
            nneg[0] += 1
        hashMap[c] -= 1

    for c in chars:
        desc(c)
    
    min_len = len(inputs) + 1
    j = 0
    for i in range(len(inputs)):
        while nneg[0] > 0:
            if j >= len(inputs):
                return min_len
            incr(inputs[j])
            j += 1
        min_len = min(min_len, j - i)
        desc(inputs[i])
    return min_len

print(smallWindow("ABBDOBEABBCCODEBANC","ABC"))
        
