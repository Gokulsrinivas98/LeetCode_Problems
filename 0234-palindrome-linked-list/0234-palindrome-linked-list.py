# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        while head:
            list.append(str(head.val))
            head = head.next
        str1=""
        string = str1.join(list)
        string2 = string[::-1]
        return string == string2