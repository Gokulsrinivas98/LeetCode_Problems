class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1, ver2 = list(map(int,version1.split('.'))) , list(map(int,version2.split('.')))
        for r1, r2 in zip_longest(ver1,ver2,fillvalue=0):
            if r1 == r2:
                continue
            return -1 if r1 < r2 else 1
        return 0
        
       