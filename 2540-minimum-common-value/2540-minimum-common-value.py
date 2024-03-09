class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        llist = set(nums1) & set(nums2)
        return min(llist) if llist else -1