class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        return nums3[len(nums3)//2] if len(nums3) % 2 != 0 else ((nums3[len(nums3)//2]+nums3[len(nums3)//2 -1])/2)