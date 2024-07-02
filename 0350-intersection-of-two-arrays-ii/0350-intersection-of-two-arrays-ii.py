class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2, r, i, j = sorted(nums1), sorted(nums2), [], 0, 0
        while i < len(n1) and j < len(n2):
            if n1[i] < n2[j]:
                i += 1
            elif n1[i] > n2[j]:
                j += 1
            else: 
                r.append(n1[i])
                i += 1
                j += 1
        return r  