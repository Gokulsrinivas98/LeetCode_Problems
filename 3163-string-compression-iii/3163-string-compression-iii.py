class Solution:
    def compressedString(self, word: str) -> str:
        result = []
        count = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1] and count < 9:
                count += 1
            else:
                result.append(f"{count}{word[i - 1]}")
                count = 1

        # Append the last counted character group
        result.append(f"{count}{word[-1]}")

        return ''.join(result)