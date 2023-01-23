class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # l=[]
        # for i in range(0,len(accounts)):
        #    l.append(sum(accounts[i]))
        # return max(l)
        
        return max(map(sum, accounts))
        