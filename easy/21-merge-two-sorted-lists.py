# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return None

        # iterate through list1 and create new list as result
        if list1 is not None and list2 is None:

            head = ListNode(list1.val)
            list1 = list1.next
            node = head

            while list1 is not None:
                node.next = ListNode(list1.val)
                node = node.next
                list1 = list1.next

            return head

        # iterate through list2 and create new list as result
        if list1 is None and list2 is not None:

            head = ListNode(list2.val)
            list2 = list2.next
            node = head

            while list2 is not None:
                node.next = ListNode(list2.val)
                node = node.next
                list2 = list2.next

            return head

        head = None
        node = None

        if list1.val <= list2.val:
            head = ListNode(list1.val)
            node = head
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            node = head
            list2 = list2.next

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                node.next = ListNode(list1.val)
                node = node.next
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                node = node.next
                list2 = list2.next

        while list1 is not None:
            node.next = ListNode(list1.val)
            node = node.next
            list1 = list1.next

        while list2 is not None:
            node.next = ListNode(list2.val)
            node = node.next
            list2 = list2.next

        return head