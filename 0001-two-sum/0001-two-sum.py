class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmaps
        seen = {}
        for i,b in enumerate(nums):
            print('b:',b)
            print('i:',i)
            a = target - b
            print('a:',a)
            if a in seen:
                return [seen[a],i]
            seen[b] = i
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # #hashmap
        # seen = {}
        # for i, b in enumerate(nums):
        #     # a + b = target -> a = target - b
        #     a = target - b
        #     if a in seen:
        #         return [seen[a], i]
        #     seen[b] = i
        