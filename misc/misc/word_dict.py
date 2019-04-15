from collections import deque


class TrieNode():
	def __init__(self, data):
		self.data = data
		self.children = {}
		self.end_of_word = False


class WordDict():
	def __init__(self):
		self.root = TrieNode(None)


	def add_word(self, word):
		tr_node = self.root
		chars = list(word)
		len_word = len(chars)
		for idx, char in enumerate(chars):
			if char not in tr_node.children:
				ch_node = TrieNode(char)
				tr_node.children[char] = ch_node
			tr_node = tr_node.children[char]
			if idx == len_word - 1:
				tr_node.end_of_word = True


	def search(self, word):
		tr_node = self.root
		chars = list(word)
		for char in chars:
			if char in tr_node.children:
				tr_node = tr_node.children[char]
			else:
				return False
		if tr_node.end_of_word:
			return True
		else:
			return False

	def search_dfs(self, word, nodes=[self.root]):
		tr_nodes = probable_nodes(word[0], nodes)
		for tr_node in tr_nodes:
			if tr_node.end_of_word:
				return True

		def probable_nodes(char, nodes):
			if word[0] == '.':
				return [child for node in nodes for child in node.children if !child.end_of_word]
			else:
				if char in nodes:
					return [nodes[char]]
				else:
					return []


	def print_words(self):
		tr_node = self.root
		while not tr_node.end_of_word:
			for key, value in tr_node.children.items():
				print(key, end='\n')
				tr_node = tr_node.children[key]


def list_try(str):
	chars = list(str)
	print(chars['a'])


if __name__ == '__main__':
	print('Word Dictionary Impl')
	word_dict = WordDict()
	word_dict.add_word('first')
	word_dict.add_word('firt')
	print(word_dict.search('fir'))
