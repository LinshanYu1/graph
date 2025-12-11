import math

import math

def extend_shortest_paths(L, W):
    """
    扩展最短路径操作：输入最多用m-1条边的距离矩阵L，输出最多用m条边的距离矩阵L'
    L: 距离矩阵（n×n）
    W: 邻接矩阵（n×n）
    返回：新的距离矩阵L'（n×n）
    """
    n = len(L)
    # 初始化结果矩阵为无穷大
    L_prime = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 遍历所有中间顶点k，计算L[i][k] + W[k][j]的最小值
            for k in range(n):
                if L[i][k] + W[k][j] < L_prime[i][j]:
                    L_prime[i][j] = L[i][k] + W[k][j]
    return L_prime

## 最外层相当于 m-1 次
def matrix_mult_shortest_paths_basic(W):
    """
    基础递推版：执行n-1次extend操作
    W: 邻接矩阵（n×n）
    返回：最终的最短路径距离矩阵
    """
    n = len(W)
    # 初始化d^(1) = W（最多用1条边）
    d = [row[:] for row in W]
    # 执行n-2次extend操作，得到d^(n-1)
    for _ in range(n - 2):
        d = extend_shortest_paths(d, W)
    return d


def matrix_mult_shortest_paths_squaring(W):
    """
    重复平方优化版：通过平方操作将时间复杂度优化为O(n^3 log n)
    W: 邻接矩阵（n×n）
    返回：最终的最短路径距离矩阵
    """
    n = len(W)
    # 初始化d^(1) = W
    d = [row[:] for row in W]
    # 需要的最大边数是n-1，通过平方操作覆盖到n-1
    m = 1
    while m < n - 1:
        d = extend_shortest_paths(d, d)  # 平方操作：d^(2m) = d^(m) ⊙ d^(m)
        m *= 2
    return d


# 示例测试
if __name__ == "__main__":
    # 定义邻接矩阵（3个顶点）
    # 顶点0: 自身0，到1权值2，到2权值7
    # 顶点1: 无出边到0，自身0，到2权值3
    # 顶点2: 无出边到0、1，自身0
    INF = math.inf
    W = [
        [0, 2, 7],
        [INF, 0, 3],
        [INF, INF, 0]
    ]

    # 基础递推版测试
    result_basic = matrix_mult_shortest_paths_basic(W)
    print("基础递推版结果：")
    for row in result_basic:
        print([x if x != INF else "∞" for x in row])

    # 重复平方优化版测试
    result_squaring = matrix_mult_shortest_paths_squaring(W)
    print("\n重复平方优化版结果：")
    for row in result_squaring:
        print([x if x != INF else "∞" for x in row])