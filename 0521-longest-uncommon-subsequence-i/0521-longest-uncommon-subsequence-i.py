class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        if a in b or b in a:
            return (max(len(a),len(b)))
        
        return (max(len(a),len(b)))