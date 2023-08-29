# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pointer = slow.next
        prev = slow.next = None
        while pointer:
            temp = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = temp

        front = head
        while prev:
            temp1, temp2 = front.next, prev.next
            front.next = prev
            prev.next = temp1
            front, prev = temp1, temp2
