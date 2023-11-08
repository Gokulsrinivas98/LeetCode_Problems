class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        path_l = path.split("/")
        result = []        
        for i in range(len(path_l)):
            if s and path_l[i] == "..":
                s.pop()
            elif path_l[i]!="" and path_l[i]!="." and path_l[i]!="..":
                s.append(path_l[i])
        if len(s) == 0:
            return "/"        
        return '/' + '/'.join( s )