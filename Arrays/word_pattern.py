class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(" ")
        if len(pattern) != len(word):
            return False
        mapPS = {}
        mapSP = {}

        for i in range(len(word)):
            c1, c2, = word[i], pattern[i]
            if c1 in mapSP and mapSP[c1] != c2 or c2 in mapPS and mapPS[c2] != c1:
                print(c1, c2)
                return False
            mapSP[c1] = c2
            mapPS[c2] = c1
        
        return True