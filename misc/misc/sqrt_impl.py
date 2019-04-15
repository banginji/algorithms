def sqrt_simple(num):
	for elem in range(num):
		if elem ** 2 > num:
			return elem - 1
		elif elem ** 2 is num:
			return elem


def sqrt_bs(num, left, right):
	mid = (left + right) // 2
	if (mid-left) <= 1:
		if mid ** 2 < num:
			return mid
		else:
			return left
	if mid ** 2 > num:
		return sqrt_bs(num, left, mid)
	else:
		return sqrt_bs(num, mid, right)

# 0 8 16
# 0 4 8
# 4 6 8
# 4 5 6


if __name__ == '__main__':
	print('Sqrt Impl')
	print(sqrt_simple(119))
	print(sqrt_bs(110, 0, 110))