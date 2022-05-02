"""
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/


Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked
 list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor
 of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to
 its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest
 element of the linked list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if root == None:
            return None

        def inorder(root1):
            nonlocal head, tale

            if root1:
                inorder(root1.left)
                if tale == None:
                    head = root1
                    tale = root1
                else:
                    tale.right = root1
                    root1.left = tale
                    tale = root1

                inorder(root1.right)

        head = None
        tale = None
        inorder(root)

        head.left = tale
        tale.right = head

        return head
