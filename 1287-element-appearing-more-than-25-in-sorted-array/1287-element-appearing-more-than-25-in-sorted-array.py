class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # n = len(arr)
        # t_n = n//4
        return Counter(arr).most_common(1)[0][0]
        
        