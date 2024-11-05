from collections import defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        word_dict = defaultdict(int)

        for word in words:
            for w in word:
                word_dict[w]+= 1
        for i, c in word_dict.items():
            if c % len(words):
                return False
        return True