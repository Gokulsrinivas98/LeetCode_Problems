class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = [0]*k
        for i in arr:
            count[i%k] += 1
        i,j = 1,k-1
        pair = 0
        while i<j:
            if count[i] != count[j]:
                return False
            pair += count[i]
            i+=1
            j-=1
        if i == j and pair > 0:
            pair += count[i]/2
        pair += count[0]/2
        return pair == len(arr)//2