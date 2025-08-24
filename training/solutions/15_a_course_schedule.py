
from typing import List
import collections

"""
Solution for: Course Schedule
"""

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    This solution uses Kahn's algorithm for topological sorting to detect a cycle.

    1.  **Build Graph and In-degrees:** We create an adjacency list to represent the
        graph and an array `in_degree` to count the number of prerequisites for each course.
    2.  **Initialize Queue:** We find all courses with an in-degree of 0 (no prerequisites)
        and add them to a queue.
    3.  **Process:** We process the queue. Each time we "take" a course (dequeue it),
        we add it to our count of completed courses. We then find all its neighbors
        (courses that depend on it) and decrement their in-degree.
    4.  **Enqueue Neighbors:** If a neighbor's in-degree becomes 0, it means all its
        prerequisites are met, and we add it to the queue.
    5.  **Final Check:** If the number of completed courses equals the total number of
        courses, it means we could finish them all (no cycle). Otherwise, a cycle
        must have prevented some courses from being taken.
    """
    adj_list = collections.defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1

    queue = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])
    courses_taken = 0

    while queue:
        course = queue.popleft()
        courses_taken += 1

        for neighbor in adj_list[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return courses_taken == numCourses
