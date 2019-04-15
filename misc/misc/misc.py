def combs(limit, base=[()], i=1):
	result = []
	for elem in base:
		if i is limit:
			result.extend([elem, elem+(i,)])
		else:
			result.extend(combs(limit, [elem, elem+(i,)], i+1))
	return result


if __name__ == '__main__':
	print('Combs')
	print(combs(4))
