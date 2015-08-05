#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} node
	# @return {void} Do not return anything, modify node in-place instead.
	@staticmethod
	def deleteNode(node):
		pNode = node
		preNode = None
		while pNode.next is not None:
			pNode.val = pNode.next.val
			preNode = pNode
			pNode = pNode.next
		preNode.next = None
	
def main():
	node1 = ListNode(1)
	node2 = ListNode(2)
	node3 = ListNode(3)
	node4 = ListNode(4)
	node1.next = node2
	node2.next = node3
	node3.next = node4
	pNode = node1
	while(pNode is not None):
		print pNode.val
		pNode = pNode.next
	print Solution.deleteNode(node3)
	pNode = node1
	while(pNode is not None):
		print pNode.val
		pNode = pNode.next

if __name__ == "__main__":
	main()
