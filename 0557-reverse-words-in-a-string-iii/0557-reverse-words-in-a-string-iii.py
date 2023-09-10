class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.split()
        # reversed_words = []
        # for word in words:
        #     reversed_words.append(word[::-1])
        # reversed_str = ' '.join(reversed_words)
        # return reversed_str
        
        words = s.split()
        length = len(words)
        for i in range(length):
            words[i] = words[i][::-1]
        return ' '.join(words)
        