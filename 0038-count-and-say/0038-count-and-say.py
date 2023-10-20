class Solution:
    def countAndSay(self, n: int) -> str:
        output = '1'
        while n > 1:
            i = j = 0
            temp = output
            output = ''
            while j < len(temp):
                if temp[i] == temp[j]:
                    j += 1
                else:
                    output += str(j-i)+ temp[i]
                    i = j
            output += str(j-i)+temp[i]
            n -= 1
        return str(output)
                
        
        