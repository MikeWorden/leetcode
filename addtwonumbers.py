
from typing import Optional                                                     

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

def link2lst(link):
    newList = []
    while link is not None:
        newList.append(link.val)
        link = link.next
    return newList

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass