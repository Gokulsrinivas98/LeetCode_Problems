class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        left = 0
        answer = []
        for i,v in enumerate(nums):
            if v == key:
                for j in range(max(left, i-k),min(len(nums), i+k+1)):
                    answer.append(j)
                left = min(len(nums),i+k+1)
                if left == len(nums):
                    break
        return answer
                