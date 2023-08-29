class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = pointer = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                pointer.next = list1.next
                list1 = list1.next
            elif list2.val < list1.val:
                pointer.next = list2.next
                list2 = list2.next
            pointer = pointer.next
            
        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2
            
        return ans.next