class Solution:
	# @param {string} s
    # @param {string} t
    # @return {boolean}
    @staticmethod
    def isAnagram(s, t):
		sS = sorted(s)
		sT = sorted(t)
		return sS == sT

def main():
	print Solution.isAnagram("anagram", "agrmaa")

if __name__ == "__main__":
	main()
