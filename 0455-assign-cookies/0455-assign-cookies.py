class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g, reverse=True)
        s=sorted(s, reverse=True)

        score=left=0
        for greed in g:
            if left<len(s) and greed<=s[left]:
                score+=1
                left+=1

        return score
                