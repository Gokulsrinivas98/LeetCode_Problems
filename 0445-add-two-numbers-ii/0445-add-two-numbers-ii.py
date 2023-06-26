# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [],[]
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        nextNode = None
        carry = 0
        
        while stack1 or stack2 or carry :
            digit1 = stack1.pop() if stack1 else 0
            digit2 = stack2.pop() if stack2 else 0
            
            digit = (digit1 + digit2 + carry)%10
            carry = (digit1 + digit2 + carry)//10
            
            node = ListNode(digit,nextNode)
            nextNode = node
        return node