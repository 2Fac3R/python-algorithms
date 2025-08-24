
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Solution for: Merge Two Sorted Lists
"""

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    This solution uses a dummy head node to build the new sorted list.

    1. Create a `dummy` node to serve as the starting point of the merged list.
    2. Create a `current` pointer, initialized to `dummy`.
    3. Loop as long as both `list1` and `list2` have nodes:
       a. Compare the values of the nodes at the head of `list1` and `list2`.
       b. Append the smaller node to `current.next`.
       c. Advance the pointer of the list from which the node was taken.
       d. Advance the `current` pointer.
    4. After the loop, one of the lists may still have remaining nodes. Append the
       rest of that non-empty list to `current.next`.
    5. Return `dummy.next`, which is the true head of the merged list.
    """
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Append the remaining part of the non-empty list
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next
