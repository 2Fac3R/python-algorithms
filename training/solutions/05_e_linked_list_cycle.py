
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Solution for: Linked List Cycle
"""

def hasCycle(head: Optional[ListNode]) -> bool:
    """
    This solution uses Floyd's Tortoise and Hare algorithm (Fast & Slow pointers).

    1. Initialize two pointers, `slow` and `fast`, both at the `head` of the list.
    2. Loop as long as `fast` and `fast.next` are not `None` (to avoid errors when
       advancing the fast pointer).
    3. In each iteration:
       a. Move `slow` one step forward (`slow = slow.next`).
       b. Move `fast` two steps forward (`fast = fast.next.next`).
    4. If at any point `slow` and `fast` point to the exact same node, it means the
       fast pointer has lapped the slow pointer, which is only possible if there
       is a cycle. We return `True`.
    5. If the loop completes (meaning `fast` reached the end of the list), then there
       is no cycle, and we return `False`.
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
            
    return False
