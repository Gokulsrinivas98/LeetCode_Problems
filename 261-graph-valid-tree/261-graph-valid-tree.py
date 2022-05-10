           
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        parent = {i:i for i in range(n)}
        
        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        for edge in edges:
            set1 = find(edge[0])
            set2 = find(edge[1])
            if set1 == set2:
                return False
            
            parent[set1] = set2
        return True