# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        maxx=0
        def helper(root,count):
            nonlocal maxx
            if root==None:
                maxx=max(count,maxx)
                count=0
                return
            count+=1
            helper(root.left,count)
            helper(root.right,count)
        helper(root,0)
        return maxx