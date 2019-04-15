def bf_combs(str):
	if len_str(str) is 0:
		return []
	result = []
	for idx, _ in enumerate(str):
		result.append(str[:idx+1])
	result.extend(bf_combs(str[1:]))
	return result


def len_str(str):
	_len = 0
	while str[_len:_len+1]:
		_len += 1
	return _len


if __name__ == '__main__':
	print('Brute Force Combinations')
	print(bf_combs('acax'))
