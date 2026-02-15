# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None

        no_duplicates_head = ListNode(head.val)
        no_duplicates_node = no_duplicates_head
        node = head

        if node.next == None:
            return no_duplicates_head

        node = node.next

        while node != None:

            curr = node.val

            while node.next != None and curr == node.next.val:
                node = node.next

            if node.next != None and curr != no_duplicates_node.val:
                no_duplicates_node.next = ListNode(curr)
                no_duplicates_node = no_duplicates_node.next

            if node.next == None and curr != no_duplicates_node.val:
                no_duplicates_node.next = ListNode(curr)

            node = node.next

        return no_duplicates_head
