class Solution:
	# @param an integer
	# @return a list of string
	@staticmethod
	def generateParenthesis(n):
		if n == 0:
			return []
		cur = "("
		ans = []
		Solution.gen_rec(ans, cur, 1, 0, n)
		return ans
	
	@staticmethod
	def gen_rec(ans, cur, left, right, n):
		# base case
		if right == n:
			ans.append(cur)
			return
		# recursive case
		if left < n:
			Solution.gen_rec(ans, cur + "(", left + 1, right, n)
		if right < left:
			Solution.gen_rec(ans, cur + ")", left, right + 1, n)
			
def main():
	print Solution.generateParenthesis(4)
	
if __name__ == "__main__":
	main()