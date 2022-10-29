
from typing import Optional                                                     

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

# helper function to convert from arrays to singly linked list
def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next
# helper function to convert from singly linked list to python list
def link2lst(link):
    newList = []
    while link is not None:
        newList.append(link.val)
        link = link.next
    return newList

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = temp = None
        carry = 0

        while l1 is not None or l2 is not None:
            total = carry
            #print("Adding carry val {}".format(carry))
            if l1 is not None:
                #print("adding l1.var {}".format(l1.val))
                total += l1.val
                l1 = l1.next

            if l2 is not None:
                #print("adding l2.var {}".format(l2.val))
                total += l2.val
                l2 = l2.next
            #print ("Sum = {}".format(total))
            node = ListNode(total % 10)
            #print("node value is {}".format(node.val))
            carry = total // 10
            #print("Carry is now {}".format(carry))

            if temp is None:
                temp = head = node
            else:
                temp.next = node
                temp = temp.next
        if carry > 0:
            temp.next = ListNode(carry)
        

        return head

#l1 = [0]
#l2 = [0]
#l1 = [2,4,3] 
#l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

l1lst = lst2link(l1)
l2lst = lst2link(l2)
sol = Solution()

atn = sol.addTwoNumbers(l1lst, l2lst)
print(link2lst(atn))

