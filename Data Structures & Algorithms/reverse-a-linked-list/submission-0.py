# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import json

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevHead = None
        currHead = head

        while currHead:
            tempHead = currHead.next
            currHead.next = prevHead
            prevHead = currHead
            currHead = tempHead

        return prevHead
        