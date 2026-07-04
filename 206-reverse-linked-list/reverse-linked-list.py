# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #in this we need to follow only 4 steps to reverse the list 
        #first we take 3 pointers 
        curr = head
        prev = None
        nxt = None

        while curr!=None:
            nxt = curr.next
            curr.next = prev # its means reverse the pointers arrow
            prev = curr
            curr = nxt
        return prev
        