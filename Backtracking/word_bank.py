from typing import List
def search(target:str, wordBanK: List[str]):
    def dfs(target, wordBank):
        print(target)
        if target =="":
            # print("here")
            return True 
        for s in wordBanK:
            if target.startswith(s):
                return dfs(target[len(s):], wordBanK)

    return dfs(target,wordBanK)

print(search("ABCD",["A","B","C","D","E"]))
print(search("entertainment",['ent', 'ert', 'ain', 'men', 't']))