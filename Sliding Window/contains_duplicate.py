from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        stack= []
        l = 0 
        r =0 
        while r < len(nums):
            if r - l > k:
                stack.pop(0)
                l += 1

            if nums[r] in stack:
                print(stack)
                return True
            stack.append(nums[r])
            r += 1
        
        return False
            
        