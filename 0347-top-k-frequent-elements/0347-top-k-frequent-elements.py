class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for num, freq in cnt.items():
            bucket[freq].append(num)
            
        bucketIdx = n
        ans = []
        while k > 0:
            while not bucket[bucketIdx]:  # Skip empty bucket
                bucketIdx -= 1
                
            for num in bucket[bucketIdx]:
                if k == 0: break
                ans.append(num)
                k -= 1
            bucketIdx -= 1
        return ans
            