class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ct = collections.Counter
        count = ct(chars)
        ans = 0
        
        for i in words:
            w_c = ct(i)
            for j in i:
                if w_c[j] > count[j]:
                    break
            else:
                ans += len(i)
        return ans
        