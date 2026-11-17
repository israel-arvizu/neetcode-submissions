# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
            
        # define the head
        head = ListNode(0)
        # track new list current
        currHeadPointer = head

        # while list 1 and list 2 are not empty
        while list1 and list2:
            # check if list 1 head <= list 2 head
            if list1.val <= list2.val:
                # point list 1 head to new list current
                currHeadPointer.next = list1
                list1 = list1.next
            # if its not
            else:
                # point list 2 head to new list current
                currHeadPointer.next = list2
                # if list 2 has next
                list2 = list2.next

            currHeadPointer = currHeadPointer.next

        currHeadPointer.next = list1 if list1 else list2

        return head.next

                    