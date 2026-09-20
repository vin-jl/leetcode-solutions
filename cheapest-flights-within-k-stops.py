class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for fr, to, cost in flights:
            adj[fr].append((to, cost)) # adj list

        dist = [[float("inf")] * (k + 10) for _ in range(n)] # dist storing k+2 cols and n rows
                                                # dist[n][c] gives cheapest way to get to node n in c flights
        dist[src][0] = 0 # getting to src node in 0 flights is free
        minheap = [(0, src, 0)] # minheap pqueue, cost, node, flights taken

        while minheap:
            cost, node, flights = heapq.heappop(minheap)
            if node == dst: return cost # found cheapest
            if flights == k+1 or dist[node][flights] < cost: continue # no more stops or stopping here is worse

            for nei, w in adj[node]:
                newcost = cost + w
                newflights = flights+1
                # check if neighbours are cool
                if dist[nei][newflights] > newcost:
                    dist[nei][newflights] = newcost
                    heapq.heappush(minheap, (newcost, nei, newflights)) # only push to mh if neighbour actually improves, since pushing a worse state (more cost) will never be better

        return -1

