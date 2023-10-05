class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1 = len(nums1)
        result = [-1]*len1
        for i in range(len1):
            index = nums2.index(nums1[i])
            for j in range(index + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    result[i] = nums2[j]
                    break

        return result