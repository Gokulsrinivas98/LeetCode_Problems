# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummylist = ListNode(0)
        dummylist.next = head
        count = 0
        d = {0:dummylist}
        
        while head:
            count += head.val
            d[count] = head
            head = head.next
        
        count = 0
        head = dummylist
        
        while head:
            count+=head.val
            head.next = d[count].next
            head = head.next
            
        return dummylist.next