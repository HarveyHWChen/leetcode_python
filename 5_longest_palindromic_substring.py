class Solution:
	# @return a string
	@staticmethod
	def longestPalindrome(s):
		if not s:
			return ""
		palin = ""
		for i in range(0, len(s)):
			thisStr = Solution.expand(s, i, i)
			if len(thisStr) > len(palin):
				palin = thisStr
			if i < len(s) - 1:
				thisStr = Solution.expand(s, i, i+1)
			if len(thisStr) > len(palin):
				palin = thisStr
		return palin
		
	# @return a integer
	@staticmethod
	def expand(s, idx1, idx2):
		while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
			idx1 -= 1
			idx2 += 1
		return s[idx1+1 : idx2]
		
def main():
	print Solution.longestPalindrome("a")
	
if __name__ == "__main__":
	main()