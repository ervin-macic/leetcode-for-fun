from typing import List 
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
            return -1
        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        while p1 < n1 and p2 < n2:
            x, y = nums1[p1], nums2[p2]
            if x == y:
                return x
            elif x > y:
                p2 += 1
            else:
                p1 += 1
        return -1