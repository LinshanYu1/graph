from collections import defaultdict

#每次dfs都更新残量图 然后直到某次dfs无法找到一条到t的路径，然后结束
class FordFulkersonDFS:
    def __init__(self):
        # 残量图，用邻接表表示
        self.res = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, cap):
        self.res[u][v] += cap
        # 初始化反向边为0
        self.res[v][u] += 0

    def dfs(self, cur, t, visited, flow):
        if cur == t:
            return flow, []

        visited.add(cur)
        for nxt in self.res[cur]:
            cap = self.res[cur][nxt]
            if cap > 0 and nxt not in visited:
                pushed, path = self.dfs(nxt, t, visited, min(flow, cap))
                if pushed > 0:
                    # 更新残量图
                    self.res[cur][nxt] -= pushed
                    self.res[nxt][cur] += pushed
                    return pushed, [(cur, nxt)] + path
        return 0, []

    def maxflow(self, s, t):
        flow = 0
        while True:
            visited = set()
            pushed, path = self.dfs(s, t, visited, float('inf'))
            if pushed == 0:
                break
            flow += pushed
            print(f"增广路径: {path}, 推流量: {pushed}")
        return flow


# -------------------------
# 测试你的图
# -------------------------
ff = FordFulkersonDFS()
edges = [
    ("S", "A", 10),
    ("A", "B", 4),
    ("B", "T", 10),
    ("A", "C", 2),
    ("A", "D", 8),
    ("D", "B", 6),
    ("S", "C", 10),
    ("C", "D", 9),
    ("D", "T", 10)
]

for u, v, c in edges:
    ff.add_edge(u, v, c)

print("最大流 =", ff.maxflow("S", "T"))
