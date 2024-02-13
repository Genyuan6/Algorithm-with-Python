给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
    
        # 辅助函数，从当前节点出发，寻找和为targetSum的路径数
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            return (curr_sum == targetSum) + dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        
        # 遍历树中的每个节点，以每个节点为起点，寻找和为targetSum的路径数
        def pathSumFromNode(node):
            if not node:
                return 0
            return dfs(node, 0) + pathSumFromNode(node.left) + pathSumFromNode(node.right)
        
        return pathSumFromNode(root)
