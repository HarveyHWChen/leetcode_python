class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	@staticmethod
	def threeSum(num):
		num.sort()
		ans = []
		i = 0
		while i < len(num):
			idx1 = i + 1
			idx2 = len(num) - 1
			while idx1 < idx2:
				cur = num[i] + num[idx1] + num[idx2]
				if cur == 0:
					curAns = [num[i], num[idx1], num[idx2]]
					ans.append(curAns)
					idx1 += 1
					idx2 -= 1
					while idx1 < idx2 and num[idx1-1] == num[idx1]:
						idx1 += 1
					while idx1 < idx2 and num[idx2+1] == num[idx2]:
						idx2 -= 1
				elif cur < 0:
					idx1 += 1
				else:
					idx2 -= 1
			i += 1
			while i < len(num) and num[i] == num[i-1]:
				i += 1
		return ans
		
def main():
	print Solution.threeSum([-1, 0, 1, 2, -1, -4])

if __name__ == "__main__":
	main()