"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node
 from the end (the list is 1-indexed).
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head1 = head

        valswap1 = 0
        valswap2 = 0

        lenl = 0
        while (head1 != None):
            if k - 1 == lenl:
                valswap1 = head1.val
            lenl += 1
            head1 = head1.next

        head1 = head
        lenl2 = 0
        while (head1 != None):
            if lenl2 == lenl - k:
                valswap2 = head1.val
            lenl2 += 1
            head1 = head1.next

        head1 = head
        lenl3 = 0
        while (head1 != None):
            if lenl3 == k - 1:
                head1.val = valswap2

            if lenl3 == lenl - k:
                head1.val = valswap1
            lenl3 += 1
            head1 = head1.next

        return head
