from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        nums1Index = {n:i for i,n in enumerate(nums1)}

        for i in range(len(nums2)):
            if nums2[i] not in nums1Index:
                # print(nums2[i])
                continue
            for j in range(i + 1, len(nums2)):
                    # print(nums2[i])
                    if nums2[j] > nums2[i]:
                        idx = nums1Index[nums2[i]]
                        res[idx] = nums2[j]
                        break
                
        return res
    
sol = Solution()
print(sol.nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))