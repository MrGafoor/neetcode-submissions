# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        f=l1
        s=l2
        addi=ListNode(0)
        curr=addi
        while f  or s:
            v1= f.val if f else 0
            v2=s.val if s else 0
            val=v1+v2+carry
            carry=0
            if val>=10:
                val=val%10
                curr.next=ListNode(val)
                carry=1
            else:
                curr.next=ListNode(val)
            f=f.next if f else f
            s=s.next if s else s
            curr=curr.next
        if carry == 1:
            curr.next=ListNode(carry)
        return addi.next

