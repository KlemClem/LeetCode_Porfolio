# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Collect all values from both lists into Python lists
        l1, l2 = [], []

        # Traverse list1
        while list1:
            l1.append(list1.val)
            list1 = list1.next

        # Traverse list2
        while list2:
            l2.append(list2.val)
            list2 = list2.next

        # Merge and sort the two lists
        final = sorted(l1 + l2)

        # Create a new linked list from the sorted values
        Linked_List = ListNode()  # Dummy node to simplify appending
        current = Linked_List

        for val in final:
            current.next = ListNode(val)
            current = current.next

        return Linked_List.next  # Return the merged sorted list  
#         Why Linked_List.next?
# The Real Start of the Merged List:
# During the list construction, you append new nodes starting with Linked_List.next. The Linked_List node itself is just a placeholder and is not part of the actual data in the merged list.