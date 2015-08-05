# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param two ListNodes
	# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		dummy = ListNode(-1)
		pNode = dummy
		while l1 and l2:
			if l1.val < l2.val:
				pNode.next = l1
				l1 = l1.next
			else:
				pNode.next = l2
				l2 = l2.next
			pNode = pNode.next
		if not l1:
			pNode.next = l2
		else:
			pNode.next = l1
		return dummy.next