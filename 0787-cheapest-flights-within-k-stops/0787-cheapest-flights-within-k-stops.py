class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, K+1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1
    
#         f = collections.defaultdict(dict)
#         for a, b, p in flights:
#             f[a][b] = p
#         heap = [(0, src, k + 1)]
      
#         while heap:
#             p, i, k = heapq.heappop(heap)
#             if i == dst:
#                 return p
#             if k > 0:
#                 for j in f[i]:
#                     # print(j)/
#                     heapq.heappush(heap, (p + f[i][j], j, k - 1))
#                     # print (heap)
             
#         return -1