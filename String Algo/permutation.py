def permutation(elems):
    for perm in recursivePerm(elems, []):
        print(perm)

def recursivePerm(elems, sofar):
    if len(elems) == 0:
        yield sofar
    else:
        for i in range(len(elems)):
            for perm in recursivePerm(elems[0:i] + elems[i + 1:],sofar + [elems[i]]):
                yield perm
def permutationByIter(elems):
    level = [elems[0]]
    for i in range(1, len(elems)):
        nList = []
        for item in level:
            nList.append(item + elems[i])
            for j in range(len(item)):
                nList.append(item[0:j] + elems[i] + item[j])
        level = nList
    return nList
# permutation("abcd")
print(permutationByIter("abcd"))