# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
# @return a ListNode
	@staticmethod
	def addTwoNumbers(l1, l2):
		head = ListNode(-1)
		pNode = head
		carry = 0
		while l1 and l2:
			pNode.next = ListNode((l1.val + l2.val + carry) % 10)
			pNode = pNode.next
			carry = (l1.val + l2.val + carry) / 10
			l1 = l1.next
			l2 = l2.next
		if not l1:
			l1 = l2
		while l1:
			pNode.next = ListNode((l1.val + carry) % 10)
			pNode = pNode.next
			carry = (l1.val + carry) / 10
			l1 = l1.next
		if carry == 1
			pNode.next = ListNode(1)
		return head.next
	
def main():
	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)
	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)
	head = Solution.addTwoNumbers(l1, l2)
	pNode = head
	while pNode:
		print pNode.val
		pNode = pNode.next
		
if __name__ == "__main__":
	main()
	