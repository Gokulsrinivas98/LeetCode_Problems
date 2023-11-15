class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = [-1] * 26
        right = [-1] * 26

        for i in range(len(s)):
            curr = ord(s[i]) - ord('a')
            if left[curr] == -1:
                left[curr] = i
            right[curr] = i

        ans = 0
        count = [False] * 26
        for i in range(26):
            if left[i] == -1:
                continue
            count = [False] * 26
            for j in range(left[i] + 1, right[i]):
                if not count[ord(s[j]) - ord('a')]:
                    count[ord(s[j]) - ord('a')] = True
                    ans += 1

        return ans