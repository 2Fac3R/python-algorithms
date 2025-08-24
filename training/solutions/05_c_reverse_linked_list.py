
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Solution for: Reverse Linked List
"""

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    This solution uses an iterative approach with two pointers: `prev` and `current`.

    1. Initialize `prev` to `None`. This will eventually be the new tail of the list.
    2. Initialize `current` to `head`.
    3. Loop as long as `current` is not `None`:
       a. Store the next node before you lose the reference: `next_node = current.next`.
       b. Reverse the pointer: `current.next = prev`.
       c. Move the pointers one step forward: `prev = current` and `current = next_node`.
    4. When the loop finishes, `current` will be `None`, and `prev` will be the new head
       of the reversed list.
    """
    prev = None
    current = head

    while current:
        next_node = current.next # Store next node
        current.next = prev     # Reverse the pointer
        prev = current         # Move prev forward
        current = next_node    # Move current forward
    
    return prev # prev is the new head
