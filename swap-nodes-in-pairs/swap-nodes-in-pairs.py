# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            temp = head.next
            head.next = self.swapPairs(temp.next)
            temp.next = head
            return temp
        return head
            
       
        
        
        
        
        
        
        
        
        
        
        
        
        # dummy = ListNode(None,head)
        # prev, curr = dummy, head
        # while curr and curr.next:
        #     prev.next = curr.next
        #     curr.next = curr.next.next
        #     prev.next.next = curr
        #     prev, curr = curr, curr.next
        # return dummy.next
        