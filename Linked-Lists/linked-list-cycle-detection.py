# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):

        slow = fast = head      # initialise

        while fast and fast.next:       # while both != None
            slow = slow.next        # slow goes one step
            fast = fast.next.next       # fast goes two steps, twice as fast

            if slow == fast:        # if equal, fast has looped around and caught up, meaning a cycle exists
                return True
    
        return False
