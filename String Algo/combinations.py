def combinationRecurs(elems, s, indx, li):
    for i in range(indx, len(elems)):
        s += elems[i]
        li.append(s)
        print(s,indx)
        combinationRecurs(elems,s, i + 1, li)

def combinationIter(elems):
    level =[""]
    for i in range(len(elems)):
        nList= []
        for item in level:
            nList.append(item+ elems[i])
        level += nList
    return nList
res = []
# combinationRecurs("abcd","",0,res)
print(combinationIter("abcd"))
# print(res)