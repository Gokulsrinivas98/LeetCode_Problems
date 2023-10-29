class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # return [[i for i in set(nums1) if i not in set(nums2)],[i for i in set(nums2) if i not in set(nums1)]]
        return [list(set(nums1)-set(nums2)),list(set(nums2)-set(nums1))]
            