from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        "10#leet4#code"
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#" and j < len(s):
                j += 1
            l = int(s[i: j])
            res.append(s[j + 1: l + j + 1])
            i = l + j + 1
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))