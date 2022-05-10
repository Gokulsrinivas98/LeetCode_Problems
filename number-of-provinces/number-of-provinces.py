class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                
            def find(self,x):
                while x!= self.root[x]:
                    x = self.root[x]
                return x
            def union(self,x,y):
                rootX, rootY = self.find(x), self.find(y)
                if rootX != rootY:
                    self.root[rootY] = x

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: 
            return 0
        s = len(isConnected)
        uf = UnionFind(s)
        for i in range(s):
            for j in range(i,s):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
                    
        return len(set([uf.find(i) for i in range(s)]))
        
        