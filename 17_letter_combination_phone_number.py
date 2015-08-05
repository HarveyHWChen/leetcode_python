class Solution:
	pad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
	# @return a list of strings, [s1, s2]
	@staticmethod
	def letterCombinations(digits):
		ans = []
		if not digits:
			return ans
		cur = ""
		Solution.combination_rec(digits, ans, cur, 0)
		return ans
        
	# @return nothing 
	@staticmethod
	def combination_rec(digits, ans, cur, level):
		if level == len(digits):
			ans.append(cur)
			return
		num = int(digits[level])
		cand = Solution.pad[num];
		for i in range(0, len(cand)):
			Solution.combination_rec(digits, ans, cur + cand[i], level+1)
		return
		
def main():
	print Solution.letterCombinations("3456")
	
if __name__ == "__main__":
	main()