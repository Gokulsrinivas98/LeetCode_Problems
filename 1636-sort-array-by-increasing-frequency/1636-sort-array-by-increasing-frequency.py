class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numDic = dict()
    
        for i in nums:
            if i in numDic:
                numDic[i]+=1
            else:
                numDic[i] = 1
        return sorted(nums, key = lambda x:(numDic[x],-x))