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


class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            # print(stack)
            cur = nums2[i]
            # print(cur)
            while stack and cur > stack[-1]:
                  val = stack.pop()
                  idx = nums1Idx[val]
                  res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res
                  
        
sol = Solution2()
print(sol.nextGreaterElement([2,4],[1,2,3,4]))