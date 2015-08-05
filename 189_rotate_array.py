class Solution:
	# @param nums, a list of integer
	# @param k, num of steps
	# @return nothing, please modify the nums list in-place.
	@staticmethod
	def rotate(nums, k):
		if not nums or k < 0:
			return
		k = k % len(num);
		if k == 0:
			return
		for i in range(0, len(nums) - k):
			
		
def main():
	nums = {1, 2, 3, 4, 5}
	rotate(nums, 3)
	print nums
	
if __name__ == "__main__":
	main()