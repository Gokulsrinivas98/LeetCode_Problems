class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        st= ""
        for i in s:
            if i not in st:
                st+=i
            else:
                st = st[st.index(i) + 1:] + i
        
            count = max(count,len(st))
        return count