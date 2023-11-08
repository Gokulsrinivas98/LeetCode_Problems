class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # n = 1
        # l = len(dist)
        # for i in range(1,l):
        #     dist = [a-b for a,b in zip(dist,speed)]
        #     print(dist)
        #     result = dist[i:]
        #     print(result)
        #     print(i,n)
        #     if not result : return n
        #     if min(result) <= 0 : return n
        #     else: n+=1
        # return n
        
        n = len(dist)
        dist = [ceil(dist[i]/speed[i]) for i in range(len(dist))]
        speed = [0]*n
        for num in dist:
            if num >= n:
                continue
            speed[num] += 1
        
        for i in range(1, len(speed)):
            speed[i] += speed[i - 1]
            if speed[i] > i:
                return i
        
        return n