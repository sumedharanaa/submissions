# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        s, result, s_new = [], [], []
        if root is not None:
            s.append(root)
            result.append(root.val)
        while True:
            for i in s:
                if i.left is not None:
                    s_new.append(i.left)
                if i.right is not None:
                    s_new.append(i.right)
            if len(s_new) == 0: break
            r = s_new[-1].val
            result.append(r)
            s = s_new
            s_new = []
        return result