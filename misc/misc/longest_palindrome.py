def longest_palindrome(str):
	max_length = 2
	list_str = list(str)
	len_str = len(str)
	for itx_max_length in range(2, len_str):
		for idx in range(len_str-itx_max_length+1):
			list_sub_str = list_str[idx: idx+itx_max_length]
			if list_sub_str == rev_list(list_sub_str):
				if itx_max_length > max_length:
					print(list_sub_str)
					max_length = itx_max_length
	return max_length


def rev_list(list_str):
	len_str = len(list_str)
	return [list_str[idx] for idx in range(len_str-1, -1, -1)]


if __name__ == '__main__':
	print('Longest Palindrome Impl')
	print(longest_palindrome('abcbddbe'))
