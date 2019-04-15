def dup(nums):
	return len(set(nums)) != len(nums)


if __name__ == '__main__':
	print('Arr Duplicate Detection Impl')
	print(dup([1, 2, 3, 4, 5, 6, 6]))
