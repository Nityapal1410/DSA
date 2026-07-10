# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.q = []
        self.front = 0   # index of front element

    def push(self, x):
        # enqueue element at the end
        self.q.append(x)

    def pop(self):
        # dequeue element from the front
        if self.size() == 0:
            return None
        x = self.q[self.front]
        self.front += 1
        return x

    def getfront(self):
        # return front element without removing
        if self.size() == 0:
            return None
        return self.q[self.front]

    def size(self):
        # current size of queue
        return len(self.q) - self.front

    def empty(self):
        return self.size() == 0

        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        queue =Queue()
        queue.push(root)
        ans.append([root.val])
        
        while queue.size()>0:
            l = queue.size()
            level =[]
            for i in range(l):
                front = queue.pop()
                if front.left!=None:
                    queue.push(front.left)
                    level.append(front.left.val)
                if front.right!=None:
                    queue.push(front.right)
                    level.append(front.right.val)
            if len(level)>0:
                ans.append(level)
        return ans