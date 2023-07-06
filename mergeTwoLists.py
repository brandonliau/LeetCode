from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def populateListNode(nums: list):
    nums.reverse()
    linkedList = None
    for i in nums:
        linkedList = ListNode(i, linkedList)
    return linkedList

def readLinkedList(ans):
    while True:
        print(ans.val)
        if ans.next == None:
            break
        ans = ans.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer = ans = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        pointer.next = list1 or list2
        return ans.next
