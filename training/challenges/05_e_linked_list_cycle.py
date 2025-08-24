
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Challenge: Linked List Cycle

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Technique:
This is the most famous application of the **Fast & Slow Two Pointers** technique in linked lists, also known as Floyd's Tortoise and Hare algorithm.
"""

def hasCycle(head: Optional[ListNode]) -> bool:
    # Your implementation here
    pass

# --- Tests ---
# (Tests for this problem are more complex as they require setting up cycles)
