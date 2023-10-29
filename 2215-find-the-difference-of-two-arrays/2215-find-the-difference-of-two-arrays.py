class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # return [[i for i in set(nums1) if i not in set(nums2)],[i for i in set(nums2) if i not in set(nums1)]]
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1-s2),list(s2-s1)]
            