import collections

def combs(n, base=[()], i=1):
	result = []
	for elem in base:
		if i is n:
			result.extend([elem + (i,), elem])
		else:
			result.extend(combs(n, [elem + (i,), elem], i+1))
	return result


def combs_alpha(str, base=[()], idx=0):
	result = []
	for elem in base:
		if idx is len(str)-1:
			result.extend([elem + (str[idx],), elem])
		else:
			result.extend(combs_alpha(str, [elem + (str[idx], ), elem], idx+1))
	return result


if __name__ == '__main__':
	print('Combinations Impl')
	print(combs_alpha(list(set('acax'))))
