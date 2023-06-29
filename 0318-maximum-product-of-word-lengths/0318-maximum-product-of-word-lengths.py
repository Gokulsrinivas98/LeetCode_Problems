class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmasks = []
        for word in words:
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))
            bitmasks.append(bitmask)

        max_product = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0:
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)
        
        return max_product
#         maxi = 0
#         for i in range(len(words)):
#             chars_i = set(words[i])
#             for j in range(i+1,len(words)):
#                 if not chars_i.intersection(set(words[j])):
#                 # if set(words[i]).isdisjoint(set(words[j])):
#                     count = len(words[i])*len(words[j])
#                     maxi= max(count,maxi)
                
#         return maxi