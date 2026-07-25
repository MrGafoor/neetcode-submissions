# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        second=slow.next
        prev=slow.next=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        first, last=head,prev
        while last:
            temp1,temp2=first.next,last.next
            first.next=last
            last.next=temp1
            first,last=temp1,temp2
            


