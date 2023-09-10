class Solution:
    def reverseVowels(self, s: str) -> str:
        words = list(s)
        start = 0
        end = len(words)-1
        vowels = 'aAeEiIoOuU'
        
        while start < end:
            while start < end and words[start] not in vowels:
                start +=1
            while start < end and words[end] not in vowels:
                end -= 1 
            words[start],words[end] = words[end],words[start]
            
            start +=1
            end -=1
        return "".join(words)