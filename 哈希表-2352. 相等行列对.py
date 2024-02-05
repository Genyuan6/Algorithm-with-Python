# 给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。
# 如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。
# 输入：grid = [[3,2,1],[1,7,6],[2,7,7]]
# 输出：1
# 解释：存在一对相等行列对：
# - (第 2 行，第 1 列)：[2,7,7]
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid) #返回的是矩阵的行数，也就是矩阵的维度
        row_hash = {}
        count = 0

        # 将每一行转换为字符串并存储在哈希表中
        for row in grid:
            row_str = ','.join(map(str, row))
            if row_str in row_hash:
                row_hash[row_str] += 1
            else:
                row_hash[row_str] = 1

        # 遍历每一列，将其转换为与行相同的字符串格式
        for j in range(n):
            col_str = ','.join(str(grid[i][j]) for i in range(n))
            if col_str in row_hash:
                count += row_hash[col_str]
        return count
