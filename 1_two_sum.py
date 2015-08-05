import sys
import getopt

class Solution:
    # @return a tuple, (index1, index2)
	@staticmethod
	def twoSum(num, target):
		map = dict()
		ans = [-1, -1]
		for i in range(0, len(num)):
			if str(target - num[i]) not in map:
				map[str(num[i])] = i
			else:
				ans[0] = min(i, map[str(target-num[i])]);
				ans[1] = max(i, map[str(target-num[i])]);
				return ans
		return ans
		
def main():
	num = [1,3,2,4,8,7,9,5,6]
	print Solution.twoSum(num, 6)
	
if __name__ == "__main__":
	main()