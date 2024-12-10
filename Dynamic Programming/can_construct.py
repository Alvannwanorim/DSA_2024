from typing import List


def canConstruct(target: str, words: List[str]):
    dp =[False] * (len(target) + 1)
    dp[0] = True
    for i in range(len(target) + 1):
        if(dp[i] == True):
            for w in words:
                # print(target[i: i + len(w)] )
                if(target[i: i + len(w)] == w and (i + len(w) <= len(target))):
                    dp[i + len(w)] = True
    # print(dp)
    return dp[len(target)]

print(canConstruct("abcdef", ["ab","abc","cd","def","abcd"]))
print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))