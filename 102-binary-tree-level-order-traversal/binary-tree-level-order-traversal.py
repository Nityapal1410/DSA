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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = [root]   # normal list used as queue
        
        while queue:
            level = []
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)   # dequeue from front
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)   # enqueue left child
                if node.right:
                    queue.append(node.right)  # enqueue right child
            
            result.append(level)

        return result