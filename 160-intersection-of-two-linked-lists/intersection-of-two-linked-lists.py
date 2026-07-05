# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA , lenB =0,0
        currA , currB =headA , headB
        while currA:
            lenA +=1
            currA = currA.next

        while currB:
            lenB +=1
            currB = currB.next

        currA, currB = headA , headB
        if lenA > lenB:
            for _ in range(lenA- lenB):
                currA = currA.next
        else:
            for _ in range(lenB- lenA):
                currB = currB.next

        while currA and currB:
            if currA == currB:
                return currA

            currA = currA.next
            currB =currB.next

        return None

        