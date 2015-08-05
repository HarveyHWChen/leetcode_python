class Solution:
	# @param haystack, a string
	# @param needle, a string
	# @return an integer
	@staticmethod
	def strStr(haystack, needle):
		i = 0
		j = 0
		while True:
			if j == len(needle):
				return i
			elif i + j >= len(haystack):
				return -1
			elif haystack[i + j] == needle[j]:
				j += 1
				continue
			else:
				i += 1
				j = 0
				
def main():
	print Solution.strStr("abcdef", "cde")
	
if __name__ == "__main__":
	main()