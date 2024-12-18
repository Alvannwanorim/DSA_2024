from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l= 0 
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[r] > height[l]:
                l +=1 
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return max_area