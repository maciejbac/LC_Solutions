# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # If l1 is empty, return l2, if l2 is empty, return l1
        if l1 == None:
            return l2
        if l2 == None:
            return l1
                
        # Compare l1 and l2 values, recursively call the function to compare next pair of values and link them together
        if l1.val <= l2.val:
            mergedList = l1
            mergedList.next = self.mergeTwoLists(l1.next, l2)
        
        else:
            mergedList = l2
            mergedList.next = self.mergeTwoLists(l1, l2.next)
            
        # Return sorted list of the values passed to the function
        return mergedList
