class Solution:
	# @return an integer
	def atoi(self, str):
		if not str:
			return 0
		sign = 1
		i = 0
		# avoid spaces upfront
		while str[i] == ' ':
			i += 1
		# sign
		if str[i] == '+':
			i+= 1
		elif str[i] == '-':
			sign = -1
			i += 1
		
		
		
		
def main():
	print atoi()
	
if __name__ == "__main__":
	main()