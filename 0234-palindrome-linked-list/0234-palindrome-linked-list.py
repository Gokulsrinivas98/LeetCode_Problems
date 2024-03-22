# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # lst = []
        # while head:
        #     lst.append(str(head.val))
        #     head = head.next
        # return lst == lst [::-1]
        
        fast,slow,rev = head,head,None
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            temp.next = rev
            rev = temp
        if fast:
            slow = slow.next
        while rev:
            if rev.val != slow.val : return False
            rev,slow = rev.next,slow.next
        return True
    