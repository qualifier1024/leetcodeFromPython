"""
LeetCode 3558: Number of Ways to Assign Edge Weights I
2026-06-11 每日一题

题目描述：
给你一棵 n 个节点的无向树，节点从 1 到 n 编号，树以节点 1 为根。
树由一个长度为 n - 1 的二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示在节点 ui 和 vi 之间有一条边。

一开始，所有边的权重为 0。你可以将每条边的权重设为 1 或 2。
两个节点 u 和 v 之间路径的代价是连接它们路径上所有边的权重之和。
选择任意一个深度最大的节点 x。返回从节点 1 到 x 的路径中，边权重之和为奇数的赋值方式数量。
由于答案可能很大，返回它对 10^9 + 7 取模的结果。
注意：忽略从节点 1 到节点 x 的路径外的所有边。

示例 1：
输入：edges = [[1,2]]
输出：1
解释：从节点 1 到节点 2 的路径有一条边（1 → 2）。
将该边赋权为 1 会使代价为奇数，赋权为 2 则为偶数。因此，合法的赋值方式有 1 种。

示例 2：
输入：edges = [[1,2],[1,3],[3,4],[3,5]]
输出：2
解释：最大深度为 2，节点 4 和节点 5 都在该深度，可以选择任意一个。
例如，从节点 1 到节点 4 的路径包括两条边（1 → 3 和 3 → 4）。
将两条边赋权为 (1,2) 或 (2,1) 会使代价为奇数，因此合法赋值方式有 2 种。

提示：
- 2 <= n <= 10^5
- edges.length == n - 1
- edges[i] = [ui, vi]
- 1 <= ui, vi <= n
- edges 表示一棵合法的树。
"""

from typing import List
from collections import deque

MOD = 10 ** 9 + 7


class Solution:
    def numberOfWays(self, edges: List[List[int]]) -> int:
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(edges) + 1

        # 构建邻接表
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS 从根节点 1 开始，计算每个节点的深度
        depth = [0] * (n + 1)
        parent = [0] * (n + 1)
        parent[1] = -1
        q = deque([1])

        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei != parent[node]:
                    parent[nei] = node
                    depth[nei] = depth[node] + 1
                    q.append(nei)

        # 最大深度（边数）
        max_depth = max(depth)

        # 深度为 L 的路径上有 L 条边，每条边可赋 1 或 2
        # 总和为奇数 ⇔ 有奇数条边赋值为 1
        # 组合数：C(L,1) + C(L,3) + ... = 2^(L-1)
        return pow(2, max_depth - 1, MOD)


# ---------- 测试代码 ----------
def test_solution():
    test_cases = [
        {
            "edges": [[1, 2]],
            "expected": 1,
        },
        {
            "edges": [[1, 2], [1, 3], [3, 4], [3, 5]],
            "expected": 2,
        },
    ]

    sol = Solution()
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = sol.numberOfWays(case["edges"])
        if result == case["expected"]:
            print(f"测试用例 {i} 通过 ✅  输出: {result}")
        else:
            print(f"测试用例 {i} 失败 ❌  期望: {case['expected']}, 实际: {result}")
            all_passed = False

    if all_passed:
        print("\n所有测试用例通过！🎉")
    else:
        print("\n存在失败的测试用例。")


if __name__ == "__main__":
    test_solution()