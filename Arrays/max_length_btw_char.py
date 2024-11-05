class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}
        res = -1
        for i, c in  enumerate(s):
            print(char_index)
            if c in char_index:
                indx = char_index[c]
                print(indx)
                res = max(res, i - indx -1)
            else:
                char_index[c] = i
        
        return res