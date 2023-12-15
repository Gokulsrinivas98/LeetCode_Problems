class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # s= set(p[0] for p in paths)
        # for path in paths:
        #     if path[1] not in s:
        #         return path[1]
        a = set()
        b = set()
        for i in paths:
            a.add(i[0])
            b.add(i[1])
        return list(b-a)[0]