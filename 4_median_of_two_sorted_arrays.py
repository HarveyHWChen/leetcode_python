class Solution:
	@staticmethod
	def findMedianSortedArrays(A, B):
		lenA = len(A)
		lenB = len(B)
		if (lenA + lenB) % 2 == 0:
			return (Solution.find_rec(A, 0, lenA-1, B, 0, lenB-1, (lenA + lenB) / 2) + Solution.find_rec(A, 0, lenA-1, B, 0, lenB-1, (lenA + lenB) / 2 + 1)) / 2.0
		else:
			return Solution.find_rec(A, 0, lenA-1, B, 0, lenB-1, (lenA + lenB) / 2 + 1)
	
	@staticmethod
	def find_rec(A, a1, a2, B, b1, b2, k):
		aLen = a2 - a1 + 1
		bLen = b2 - b1 + 1
		if aLen > bLen:
			return Solution.find_rec(B, b1, b2, A, a1, a2, k)
		if aLen == 0:
			return B[b1 + k - 1]
		if k == 1:
			return min(A[a1], B[b1])
		numA = min(aLen, k / 2)
		numB = k - numA
		if A[a1 + numA - 1] < B[b1 + numB - 1]:
			# throw away first half of A
			return Solution.find_rec(A, a1 + numA, a2, B, b1, b1 + numB, k - numA)
		else:
			return Solution.find_rec(A, a1, a1 + numA, B, b1 + numB, b2, k - numB)
		
def main():
	A = []
	B = [1, 2, 3, 4, 5]
	print Solution.findMedianSortedArrays(A, B)
	
if __name__ == "__main__":
	main()