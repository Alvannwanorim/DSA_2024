from typing import List


def countConstruct(target: str, words: List[str]):
    dp = [0] * (len(target) + 1)
    dp[0] = 1
    for i in range(len(target) + 1):
        if dp[i] > 0:
            for w in words:
                if target[i: i + len(w)] == w and ((i + len(w))<= len(target)):
                    dp[i + len(w)] += dp[i]
    print(dp)
    return dp[len(target)]
print(countConstruct("purple", ["purp","p","ur","le","purpl"]))
