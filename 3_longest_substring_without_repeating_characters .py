class Solution:
	# @return an integer
	@staticmethod
	def lengthOfLongestSubstring(s):
		if not s:
			return 0
		dic = set()
		maxLen = 0
		left = 0
		right = 0
		while(right < len(s)):
			if s[right] in dic:
				if right - left > maxLen:
					maxLen = right - left
				while s[right] != s[left]:
					dic.remove(s[left])
					left += 1
				left += 1
			else:
				dic.add(s[right])
			right += 1
		maxLen = max(maxLen, right - left)
		return maxLen

def main():
	print Solution.lengthOfLongestSubstring("absgceidadc")
	
if __name__ == "__main__":
	main()