class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # count = 0
        # new_a = ""
        # while len(new_a) <= 10000:
        #     if b not in new_a:
        #         new_a+=a
        #         count+=1
        #     else:
        #         return count
        # return -1
        
        if len(a) == 0 :
            return -1
        rep = math.ceil(len(b)/len(a))
        for i in range(2):
            if b in a*rep:
                return rep
            rep +=1
        return -1