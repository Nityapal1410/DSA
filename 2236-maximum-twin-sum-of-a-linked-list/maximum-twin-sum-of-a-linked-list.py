# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #Approach (Step by Step)
#Middle find karo → slow/fast pointer se.

#Second half reverse karo → standard linked list reversal.

#Compare halves → first half aur reversed second half ke nodes ko pair karke sum nikalo.

#Max sum track karo → har pair ka sum check karke maximum store karo
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left , right = head , prev
        max_sum = (0)
        while right:
            max_sum = max(max_sum , left.val + right.val)
            left = left.next
            right = right.next
        return max_sum


        