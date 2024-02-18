n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。
路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。
今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。
请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。
题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。
示例 1：
输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
        
        # 构建图，包括正向边和反向边，反向边用于标记需要改变方向
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # 正向边，需要改变方向
            graph[b].append((a, 0))  # 反向边，不需要改变方向

        # DFS遍历图，计算需要改变方向的边的数量
        def dfs(city, visited):
            visited.add(city)
            change_directions = 0
            for next_city, needs_change in graph[city]:
                if next_city not in visited:
                    change_directions += needs_change
                    change_directions += dfs(next_city, visited)
            return change_directions
    
        # 从城市0开始遍历
        return dfs(0, set())
