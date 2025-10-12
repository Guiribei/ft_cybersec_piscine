import sys

def main(args):
	isRecursive = False
	recursionDepth = 1
	url = None
	saveDest = "./data/"

	for i, arg in enumerate(args):
		if arg == '-r':
			isRecursive = True
		if arg == '-l':
			try:
				recursionDepth = int(args[i + 1])
			except (IndexError, ValueError):
				recursionDepth = -1


	return (isRecursive, recursionDepth, url, saveDest)


if __name__ == '__main__':
	isRecursive, recursionDepth, url, saveDest = main(sys.argv[1:])

	print(f"Is recursive: {isRecursive}")
	print(f"Recursion depth: {recursionDepth}")
	print(f"URL: {url}")
	print(f"Save destination: {saveDest}")
