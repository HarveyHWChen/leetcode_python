# stk for ()

class Solution:
	# @return a boolean
	@staticmethod
	def isValid(s):
		stk = []
		for i in range(0, len(s)):
			if s[i] == '(':
				stk.append('(')
			elif s[i] == ')':
				if not stk or stk[len(stk)-1] != '(':
					return False
				else:
					stk.pop()
			elif s[i] == '[':
				stk.append('[')
			elif s[i] == ']':
				if not stk or stk[len(stk)-1] != '[':
					return False
				else:
					stk.pop()
			elif s[i] == '{':
				stk.append('{')
			elif s[i] == '}':
				if not stk or stk[len(stk)-1] != '{':
					return False
				else:
					stk.pop()
		return not stk
	
def main():
	print Solution.isValid(")(){}[][]")
	
if __name__ == "__main__":
	main()