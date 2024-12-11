from typing import List


def allConstruct(target: str, words: List[str]):
    dp = [[] for _ in range (len(target) + 1)]
    dp[0] = [[]]

    for i in range(len(target) + 1):
        for w in words:
            if(target[i: i + len(w)] == w and (i+ len(w))<= len(target)):
                comb = [x + [w] for x in dp[i]]
                # print(comb)
                dp[i + len(w)].extend(comb)
    return dp[len(target)]

print(allConstruct("purple", ["purp","p","ur","le","purpl"]))

