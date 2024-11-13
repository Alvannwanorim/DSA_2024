def combinationRecurs(elems, s, indx, li):
    for i in range(indx, len(elems)):
        s += elems[i]
        li.append(s)
        print(s,indx)
        combinationRecurs(elems,s, i + 1, li)

def combinationIter(elems):
    pass

res = []
combinationRecurs("abcd","",0,res)
print(res)