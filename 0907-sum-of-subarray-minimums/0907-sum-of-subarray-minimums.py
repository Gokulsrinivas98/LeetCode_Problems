class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # mini = 0
        # mod = 10**9 + 7
        # def subarray(arr,start,end):
        #     nonlocal mini
        #     if end == len(arr):
        #         return
        #     elif start > end: 
        #         return subarray(arr,0,end+1)
        #     else:
        #         mini += min(arr[start:end+1])
        #         return subarray(arr,start+1,end)
        # subarray(arr,0,0)
        # return mini%mod
        
        MOD = 10**9 + 7
        stack = []
        sumOfMinimums = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                leftBoundary = stack[-1] if stack else -1
                rightBoundary = i

                count = (mid - leftBoundary) * (rightBoundary - mid) % MOD

                sumOfMinimums += (count * arr[mid]) % MOD
                sumOfMinimums %= MOD
            stack.append(i)

        return int(sumOfMinimums)