class Solution:
    def valid_parenthesis(self, strs: str):
        stack = []
        opening_params = ['(','{','[']
        closing_params = [')','}',']']
        hash_table = {')':'(', '}':'{', ']':'['}

        for s in strs:
            if s in opening_params:
                stack.append(s)
            elif s in closing_params:
                pair = stack.pop()
                if hash_table[s] != pair:
                    print(hash_table[s], pair)
                    return False
        return True  if not stack else False
                
sol = Solution()
print(sol.valid_parenthesis("[]"))
print(sol.valid_parenthesis("([{}])"))
print(sol.valid_parenthesis("([{}]"))