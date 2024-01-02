class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        s = list(s)
        s.sort(key=lambda x:(-c[x],x))
        return ''.join(s)