给定二叉搜索树（BST）的根节点 root 和一个整数值 val。
你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。
示例 1:
输入：root = [4,2,7,1,3], val = 2
输出：[2,1,3]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 如果根节点为空，或者找到了值为val的节点，返回该节点
        if root is None or root.val == val:
            return root
        
        # 如果val小于当前节点的值，搜索左子树
        if val < root.val:
            return self.searchBST(root.left, val)
        # 如果val大于当前节点的值，搜索右子树
        else:
            return self.searchBST(root.right, val)
    # 为了展示结果，我们需要一个辅助函数来以列表形式返回BST
    def bstToList(root):
        if root is None:
            return []
        return [root.val] + bstToList(root.left) + bstToList(root.right) #前序遍历
