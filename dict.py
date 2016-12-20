from sys import argv
from DictionaryServices import DCSCopyTextDefinition

def main():
	word = argv[1]
	result = DCSCopyTextDefinition(None, word, (0, len(word)))
	try:
		result = result.split('.')
		for row in result:
			print(row)
	except:
		print('その単語は辞書に登録されていません')

if __name__ == '__main__':
	main()