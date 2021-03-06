class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True
        dp = {}
        for i, j in zip(str1, str2):
            if dp.setdefault(i, j) != j:
                return False
        return len(set(str2)) < 26

# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value, see example below