# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
               
        while(current): # Continue as long as current exists
        
            if(not current.next): # Break if working on the last node in the list
                break
        
            if current.val == current.next.val: # Compare the value of the current node to the value of current+1 node
                current.next = current.next.next  # If the values are the same, replace the link with the link to the current+2 node
            else:
                current = current.next # If the values don't match, move onto the next node in the list
            
        return head # Return the first node of the list
        
        
        
