# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next is None:
            return False
        oneStepPointer = head
        twoStepPointer = head.next

        while oneStepPointer is not None or twoStepPointer is not None:
            if oneStepPointer == twoStepPointer:
                return True
            oneStepPointer = oneStepPointer.next
            if twoStepPointer and twoStepPointer.next:
                twoStepPointer = twoStepPointer.next.next
            else: 
                twoStepPointer = None

        return False
        