class Solution:
    def swap(self, c, added,removed):
        c[added]+=1
        c[removed] -=1
        
        if c[removed] <=0:
            del c[removed]
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        for i in string.ascii_lowercase: #For loop from a -> z
            for j in string.ascii_lowercase: #For loop from a -> z
                if i not in c1 or j not in c2: #If the letters not in counters, skip
                    continue
                self.swap(c1,j,i)              #else swap
                self.swap(c2,i,j)
                if len(c1) == len (c2):         #if length of counter is same after swap return true
                    return True                                     
                self.swap(c1,i,j)               #else reverse changes
                self.swap(c2,j,i)
                
        return False
        # for i in range(len(word1)):
        #     for j in range(len(word2)):
        #         word1_list = list(word1)
        #         word2_list = list(word2)
        #         word1_list[i], word2_list[j] = word2_list[j], word1_list[i]
        #         if len(set(word1_list)) == len(set(word2_list)):
        #             return True
        # return False