import heapq
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param a list of ListNode
	# @return a ListNode
	@staticmethod
	def mergeKLists(lists):
		pool = []
		for i in range(0, len(lists)):
			heapq.heappush(pool, lists[i])
		dummy = ListNode(-1)
		pNode = dummy
		while pool:
			cur = heapq.heappop(pool)
			if cur.next:
				heapq.heappush(pool, cur.next)
			pNode.next = cur
			pNode = pNode.next
		return dummy.next
		
def main():
	list1 = ListNode(1)
	list1.next = ListNode(4)
	list1.next.next = ListNode(7)
	list2 = ListNode(2)
	list2.next = ListNode(5)
	list2.next.next = ListNode(8)
	list3 = ListNode(3)
	list3.next = ListNode(6)
	list3.next.next = ListNode(9)
	lists = [list1, list2, list3]
	ans = Solution.mergeKLists(lists)
	while ans:
		print ans.val
		ans = ans.next
		
if __name__ == "__main__":
	main()
