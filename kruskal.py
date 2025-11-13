import heapq



class UnionFind:
    def __init__(self, vertices):
        self.parent = {v :v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    # find root of x
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    # union two vertices
    def union(self, x, y):
        x_root =self.find(x)
        y_root =self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else :
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return True

# priority queue store every edge (weight, edge_start, edge_end)
# support condition that some edges have been choosed
def kruskal(graph, choosed_edges):

    # init un
    vertices = set(graph.keys())
    for node in graph:
        for nb, _ in graph[node]:
            vertices.add(nb)
    v_number = len(vertices)
    uf=UnionFind(vertices)

    # check choosed_edges
    mst_edges = []
    def is_edge_valid(u, v):
        return any(nb == v for (nb, _) in graph.get(u, [])) or any(nb == u for (nb, _) in graph.get(v, []))

    for u, v in choosed_edges:
        if is_edge_valid(u, v):
            if uf.union(u, v):
                mst_edges.append((u, v))

    # priority queue records other edges
    pq = []
    edges = set()
    for u in graph:
        for v, weight in graph[u]:
            edge_key = frozenset((u, v))
            if edge_key not in edges and (u, v) not in choosed_edges and (v, u) not in choosed_edges:
                heapq.heappush(pq, (weight, u, v))
                edges.add(edge_key)


    # greedy policy: pop from pq and union
    while pq and len(mst_edges) < v_number - 1:
        weight, u, v = heapq.heappop(pq)
        if uf.union(u, v):
            mst_edges.append((u, v))

    if len(mst_edges) != v_number - 1:
        raise ValueError("graph is disconnected")
    return mst_edges