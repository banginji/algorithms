from math import sqrt, ceil


def gen_primes(n):
	nums = [True] * n
	for idx in range(2, ceil(sqrt(n))):
		if not nums[idx]:
			continue
		for elem in range(idx+idx, n, idx):
			nums[elem] = False
	print([idx for idx, elem in enumerate(nums) if elem][2:])


if __name__ == '__main__':
	print('Generate Primes')
	gen_primes(100)
