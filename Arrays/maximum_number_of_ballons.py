from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        pattern = Counter("balloon")
        textCount = Counter(text)
        res = len(text)
        for s in pattern:
            res = min(res, textCount[s] // pattern[s])
        
        return res