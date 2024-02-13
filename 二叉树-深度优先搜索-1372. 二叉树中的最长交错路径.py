# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_length = 0

        # DFS函数，返回从当前节点开始向左和向右的最长交错路径长度
        def dfs(node, isLeft):
            nonlocal max_length
            if not node:
                return -1
            # 计算左子节点的左向和右向最长交错路径
            left = dfs(node.left, True)
            # 计算右子节点的左向和右向最长交错路径
            right = dfs(node.right, False)
            # 更新全局最长交错路径长度
            max_length = max(max_length, left + 1, right + 1)
            # 如果当前方向是左，则返回右向路径长度加一；否则返回左向路径长度加一
            return right + 1 if isLeft else left + 1

        dfs(root, True)
        dfs(root, False)
        return max_length
