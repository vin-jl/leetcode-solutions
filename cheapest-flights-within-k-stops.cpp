class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int, int>>> adj(n);
        for(auto flight : flights){
            adj[flight[0]].emplace_back(flight[1], flight[2]);
        }
        queue<pair<int, pair<int, int>>> q;
        vector<int> dist(n, INT_MAX);

        q.push({src, {0, 0}});
        dist[src] = 0;
        while(!q.empty()){
            auto cur = q.front();
            q.pop();
            int node = cur.first;
            int price = cur.second.first;
            int stops = cur.second.second;

            if(stops > k) continue;

            for(auto i : adj[node]){
                int next = i.first;
                int cost = i.second;

                if(price + cost < dist[next]){
                    dist[next] = price + cost;
                    q.push({next, {dist[next], stops + 1}});
                }
            }
        }
        return dist[dst] == INT_MAX ? -1 : dist[dst];
    }
};
