# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
HashSet Approach: O(n) O(n)
keep track of visited nodes in a hashset

Slow and Fast Pointers Approach: O(n), O(1)
fast will eventually catch up as the gap between the slow and fast pointers decreases
by 1 for every iteration (+1-2). It will take n (# of nodes) to catch up
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
   #Time complexity: O(n)
   #Space complexity: O(1)