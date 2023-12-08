class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c = collections.Counter(s)
        mini = inf
        for i,count in Counter(target).items():
                mini = min(mini,c[i]//count)
        return mini
    