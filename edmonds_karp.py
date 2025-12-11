from collections import deque, defaultdict

# 每次bfs找到一个到t的路径就退出 并更新残量图，然后继续bfs，直到某次bfs找不到t
class EdmondsKarp:
    def __init__(self):
        # 残量图，用邻接表表示
        self.res = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, cap):
        self.res[u][v] += cap
        # 反向边初始化为 0
        self.res[v][u] += 0

    def bfs(self, s, t, parent):
        """BFS 返回是否存在增广路径，并用 parent 记录路径"""
        visited = set()
        queue = deque()
        queue.append(s)
        visited.add(s)
        while queue:
            u = queue.popleft()
            for v in self.res[u]:
                if v not in visited and self.res[u][v] > 0:
                    visited.add(v)
                    parent[v] = u
                    if v == t:
                        return True
                    queue.append(v)
        return False

    def maxflow(self, s, t):
        flow = 0
        parent = {}
        while True:
            parent = {}
            found = self.bfs(s, t, parent)
            if not found:
                break

            # 找到路径上的最小残量
            path_flow = float('inf')
            v = t
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.res[u][v])
                v = u

            # 更新残量图
            v = t
            path = []
            while v != s:
                u = parent[v]
                self.res[u][v] -= path_flow
                self.res[v][u] += path_flow
                path.append((u, v))
                v = u

            flow += path_flow
            print(f"增广路径: {path[::-1]}, 推流量: {path_flow}")

        return flow

# -------------------------
# 测试你的图
# -------------------------
ek = EdmondsKarp()
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
    ek.add_edge(u, v, c)

print("最大流 =", ek.maxflow("S", "T"))
