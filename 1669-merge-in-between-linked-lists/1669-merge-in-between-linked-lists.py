# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr1 = list1 
        for _ in range(1,a): ptr1 = ptr1.next
        ptr2 = ptr1
        while b >= a: ptr2 = ptr2.next; b -= 1
        ptr1.next = list2
        while list2.next != None: list2 = list2.next
        list2.next = ptr2.next
        return list1
        
        