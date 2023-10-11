class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 0
        new_a = ""
        while len(new_a) <= 10000:
            if b not in new_a:
                new_a+=a
                count+=1
            else:
                return count
        return -1
        