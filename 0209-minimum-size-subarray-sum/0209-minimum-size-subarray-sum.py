class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        subarray_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            subarray_sum += nums[right]

            while subarray_sum >= target:
                min_length = min(min_length, right - left + 1)
                subarray_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0