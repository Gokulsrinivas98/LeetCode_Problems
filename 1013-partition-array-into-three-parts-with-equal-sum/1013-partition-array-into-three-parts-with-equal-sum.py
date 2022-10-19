class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        [average,remainder,count,partition] = [sum(arr)//3, sum(arr)%3,0,0]
        for a in arr:
            partition += a
            if partition == average:
                count += 1
                partition = 0
        return not remainder and count>=3
                