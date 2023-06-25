# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resulthead = ListNode(0)
        resulttail = resulthead
        carry = 0
        
        while l1 is not None or l2 is not None or carry!=0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0
            
            digit = (digit1 + digit2 + carry)%10
            carry = (digit1 + digit2 + carry)//10
            
            newNode = ListNode(digit)
            resulttail.next = newNode
            resulttail = resulttail.next
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            
        result = resulthead.next
        resulthead.next = None
        return result