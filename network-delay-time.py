class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+2)]
        for fr, to, cost in times:
            adj[fr].append([to, cost])
        dist = [float("inf")] * (n+2)
        dist[k] = 0
        mh = [[0, k]]
        while mh:
            cost, node = heapq.heappop(mh)
            if dist[node] < cost: continue

            for nei, w in adj[node]:
                nextCost = cost + w
                if dist[nei] > nextCost:
                    dist[nei] = nextCost
                    heapq.heappush(mh, [nextCost, nei])
        
        ans = max(dist[1:n+1])

        if ans == float("inf"):
            return -1

        return ans
