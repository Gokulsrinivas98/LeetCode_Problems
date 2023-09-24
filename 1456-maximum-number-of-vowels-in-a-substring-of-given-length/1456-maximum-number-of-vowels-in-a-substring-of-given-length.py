class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(char):
            return char in 'aeiouAEIOU'
        max_vowels = 0
        current_vowels = 0

        # Calculate vowels in the first window of length k
        for i in range(k):
            if is_vowel(s[i]):
                current_vowels += 1

        max_vowels = current_vowels

        # Slide the window and update max_vowels
        for i in range(k, len(s)):
            if is_vowel(s[i]):
                current_vowels += 1
            if is_vowel(s[i - k]):
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels