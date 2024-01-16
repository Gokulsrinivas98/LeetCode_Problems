class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wl = list(zip(*matches))
        lostzero = set(wl[0])
        lostone = []
        
        count = Counter(wl[1])
        
        for key in count.keys():
            if count[key] > 0 and key in lostzero:
                lostzero.remove(key)
            if count[key] == 1:
                lostone.append(key)
        return [sorted(list(lostzero)),sorted(lostone)]