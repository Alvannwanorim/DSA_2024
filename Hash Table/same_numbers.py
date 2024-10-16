from typing import List


def sameNumbers(nums1: List[int], nums2: List[int]):
    if len(nums1) != len(nums2):
        return False
    nums1.sort()
    nums2.sort()
    l = r = 0

    while l < len(nums1):
        if nums1[l] != nums2[r]:
            return False
        l += 1
        r += 1
    return True


print(sameNumbers([1,2,3,3,4,5],[1,2,3,3,4,5]))
print(sameNumbers([1,2,3,3,4,5],[1,2,3,3,4,4]))