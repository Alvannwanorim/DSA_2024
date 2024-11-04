from collections import Counter, defaultdict
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0
        for word in words:
            w_count = defaultdict(int)
            good = True
            for w in word:
                w_count[w] += 1
                if w not in count or w_count[w] > count[w]:
                    good = False
                    break
                
            if good: res += len(word)
        return res