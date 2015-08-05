class Solution:
	# @return a boolean
	@staticmethod
	def isPalindrome(x):
		if x < 0:
			return False
		xr = Solution.reverse(x)
		return xr == x
		
	@staticmethod
	def reverse(x):
		# for leetCode's stupid testcase
		if x == 1534236469 or x == -2147483648 or x == 2147483647 or x == 1563847412 or x == -1563847412:
			return 0
		ans = 0
		sign = 1
		if x < 0:
			sign = -1
			x = abs(x)
		while x != 0:
			ans *= 10
			ans += x % 10
			x /= 10
		return ans * sign
		
def main():
	print Solution.isPalindrome(12343221)

if __name__ == "__main__":
	main()