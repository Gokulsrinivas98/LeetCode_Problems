# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
            
        
#         def rev (start, end, ls):
#             if start >= end:
#                 return
#             ls[start],ls[end] = ls[end],ls[start]
            
#             rev(start+1,end-1,ls)
#         rev(0,len(head)-1,head)
            
        