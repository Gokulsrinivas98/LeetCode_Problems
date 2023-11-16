class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maximum = 0
        for word in strs:
            if any(ord(letter) in range(97, 123) for letter in word):
                if len(word) > maximum:
                    maximum = len(word)
            else:
                if int(word) > maximum:
                    maximum = int(word)
        return maximum