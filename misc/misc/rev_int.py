def rev_int(num):
	list_str = list(str(num))
	len_str = len(list_str)
	if list_str[0] is '-':
		res_list = [list_str[idx] for idx in range(len_str-1, 0, -1)]
	else:
		res_list = [list_str[idx] for idx in range(len_str-1, -1, -1)]
	res_str = ''.join([elem for elem in res_list])
	res_int = int(res_str)
	return -res_int if list_str[0] is '-' else res_int


if __name__ == '__main__':
	print('Reverse Integer Impl')
	print(rev_int(123))
