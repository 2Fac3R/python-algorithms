
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Challenge: Merge Two Sorted Lists

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Technique:
This problem is best solved using a **Dummy Head Node** (or sentinel node). This simplifies the logic because you don't have to handle the edge case of inserting into an empty list. You create a dummy node, build the new list off of it, and return `dummy.next` at the end.
"""

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Your implementation here
    pass

# --- Helper functions for testing (omitted for brevity, same as previous challenge) ---

# --- Tests ---
# (Tests would be structured similarly to the previous challenge)
