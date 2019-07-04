# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        interval=1
        tot=len(lists)
        if tot==0:
            return None
        while interval<tot:
            for i in range(0,tot-interval,interval*2):
                lists[i]=self.merge2Lists(lists[i],lists[i+interval])
            interval*=2
        return lists[0]

    def merge2Lists(self,first,second):
        head=dummy=ListNode(-1)
        while first and second:
            if first.val>second.val:
                head.next=second
                head=head.next
                second=second.next
            else:
                head.next=first
                head=head.next
                first=first.next
        rest=first or second
        while rest:
            head.next=rest
            head=head.next
            rest=rest.next
        return dummy.next