class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_avg = window_sum / k

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, window_sum / k)

        return max_avg
        
        # if len(nums) == k:
        #     return sum(nums)/k
        # maxavg = float('-inf')
        # for i in range(len(nums)-k+1):
        #     maxavg = max(maxavg,sum(nums[i:i+k])/k)
        # return maxavg