from typing import List
def search(target:str, wordBanK: List[str]):
    def dfs(target):
        if target == "":
            return
        res = []
        for s in wordBanK:
            if target.startswith(s):
                x = target[:len(s)]
                if x == target:
                    res += [x]
                else: 
                    for y in dfs(target[len(x):]):
                        res+= [x + ' ' + y]
        return res
    return dfs(target)
print(search("entertainment",['ent', 'ert', 'ain', 'men', 't', 'ment','enter']))
print(search('catsanddog', ["cat","cats","and","sand","dog"]))
