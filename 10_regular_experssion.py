class Solution:
	# @return a boolean
	@staticmethod
	def isMatch(s, p):
		if not p:
			return not s
		if len(p) == 1 or p[1] != '*':
			if len(s) == 0 or (p[0] != '.' and s[0] != p[0]):
				return False
			return Solution.isMatch(s[1:], p[1:])
		else:
			sLen = len(s)
			i = -1
			while i < sLen and (i < 0 or p[0] == '.' or s[i] == p[0]):
				if Solution.isMatch(s[i+1:], p[2:]):
					return True
				i += 1
			return False
		
def main():
	print Solution.isMatch("aaaaabaccbbccababa", "a*b*.*c*c*.*.*.*c")
	
if __name__ == "__main__":
	main()