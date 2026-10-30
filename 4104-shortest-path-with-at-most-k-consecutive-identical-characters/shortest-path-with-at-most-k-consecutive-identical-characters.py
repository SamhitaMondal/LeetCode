class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph=[[] for _ in range(n)]
        for u,v,w in edges:
            graph[u].append((v,w))
        INF=float('inf')
        dist=[[INF]*(k+1)for _ in range(n)]
        dist[0][1]=0
        pq=[(0,0,1)]
        while pq:
            cost,u,streak=heapq.heappop(pq)
            if cost!=dist[u][streak]:
                continue
            if u == n - 1: 
                return cost 
            for v, w in graph[u]: 
                if labels[u] == labels[v]: 
                    new_streak = streak + 1 
                else: 
                    new_streak = 1 
                if new_streak > k: 
                    continue 
                new_cost = cost + w 
                if new_cost < dist[v][new_streak]: 
                    dist[v][new_streak] = new_cost 
                    heapq.heappush(pq, (new_cost, v, new_streak))
        return -1       