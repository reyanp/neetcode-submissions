# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev, curr = head, head
        
        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next
            if prev == curr:
                return True
        return False

'''
1 2 3 4 2 5
5 --> 2

prev 1 2 3 4 1 2 3 4
curr 2 3 2 4

'''