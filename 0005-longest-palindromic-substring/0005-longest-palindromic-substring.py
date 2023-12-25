class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Transform the input string by inserting '#' between each character
        # For example, "babad" becomes "#b#a#b#a#d#"
        # This is to handle both even and odd length palindromes
        t = '#'.join(f'#{s}#')
        n = len(t)
       
        
        # Create an array to store the length of the palindrome centered at each character
        p = [0] * n
        # Initialize the center and the right boundary of the current palindrome
        c = 0
        r = 0
        # Initialize the center and the length of the longest palindrome
        max_c = 0
        max_len = 0
        # Loop through the transformed string
        for i in range(0, n - 1):
            # Find the mirror index of i with respect to the center c
            # For example, if c = 5 and i = 7, then j = 3
            j = 2 * c - i
            # If i is within the right boundary, use the minimum of the mirror value and the distance to the boundary
            # Otherwise, set the palindrome length to 0
            if i < r:
                p[i] = min(r - i, p[j])
            else:
                p[i] = 0
            # Try to expand the palindrome around i
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
            # If the expanded palindrome exceeds the right boundary, update the center and the boundary
            if i + p[i] > r:
                c = i
                r = i + p[i]
            # If the expanded palindrome is longer than the current longest, update the center and the length
            if p[i] > max_len:
                max_c = i
                max_len = p[i]
        # Return the longest palindromic substring by removing the '#' characters
        return t[max_c - max_len : max_c + max_len + 1].replace('#', '')