
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Challenge: Reverse Linked List

Given the `head` of a singly linked list, reverse the list, and return the new head.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Technique:
This is a classic linked list problem that uses the **"Previous and Current" pointer pattern**. You iterate through the list, and for each node, you reverse the direction of its `next` pointer to point to the `prev` node.
"""

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # Your implementation here
    pass

# --- Helper functions for testing ---
def list_to_nodes(nodes_list):
    if not nodes_list:
        return None
    head = ListNode(nodes_list[0])
    current = head
    for val in nodes_list[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def nodes_to_list(head):
    nodes = []
    current = head
    while current:
        nodes.append(current.val)
        current = current.next
    return nodes

# --- Tests ---
def run_tests():
    test_cases = [
        ([1,2,3,4,5], [5,4,3,2,1]),
        ([1,2], [2,1]),
        ([], []),
    ]

    for i, (input_list, expected_list) in enumerate(test_cases):
        head = list_to_nodes(input_list)
        result_head = reverseList(head)
        result_list = nodes_to_list(result_head)
        if result_list == expected_list:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected_list}, got {result_list}")

if __name__ == "__main__":
    run_tests()
