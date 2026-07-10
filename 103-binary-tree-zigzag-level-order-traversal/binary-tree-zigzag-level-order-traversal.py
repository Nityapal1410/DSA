# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans =[]
        if root is None:
            return []
        queue = [root]
        ans.append([root.val])

        while len(queue)>0:
            l = len(queue)
            level=[]
            for i in range(l):
                front = queue.pop(0)
                if front.left!=None:
                    queue.append(front.left)
                    level.append(front.left.val)
                if front.right!=None:
                    queue.append(front.right)
                    level.append(front.right.val)

            if len(level)>0:
                if len(ans)%2 ==1:
                    level.reverse()
                ans.append(level)
        return ans


            
    
        