import argparse

parser = argparse.ArgumentParser(description='Search for words including partial words')
parser.add_argument('snippet', help='enter partial or complete string to search for..')
args = parser.parse_args()


snippet = args.snippet.lower()
words = open ('/usr/share/dict/words','r')
print([word.strip() for word in words if snippet in word.lower()])

words.close()