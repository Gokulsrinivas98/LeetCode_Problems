class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = 0
        counter = Counter(stones)
        for i in counter:
            if i in jewels:
                s+=counter[i]
        return s