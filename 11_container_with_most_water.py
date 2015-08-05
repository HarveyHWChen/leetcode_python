class Solution:
	# @return an integer
	@staticmethod
	def maxArea(height):
		most = 0
		idx1 = 0
		idx2 = len(height) - 1
		while idx1 < idx2:
			thisArea = min(height[idx1], height[idx2]) * (idx2 - idx1)
			if thisArea > most:
				most = thisArea
			if height[idx1] > height[idx2]:
				idx2 -= 1
			else:
				idx1 += 1
		return most

def main():
	height = [1, 2, 3, 2, 2]
	print Solution.maxArea(height)
	
if __name__ == "__main__":
	main()