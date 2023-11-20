class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # if len(nums) == k: return nums
        # numss = sorted(nums)
        # res = []
        # print(numss[-k:])
        # for i in nums :
        #     if i in numss[-k:] and len(res) < k :
        #         res.append(i)
        # return res
        return [n for i, n in sorted(sorted(enumerate(nums), key=lambda e: -e[1])[:k])]