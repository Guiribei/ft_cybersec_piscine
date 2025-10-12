import sys
from pathlib import Path

def main(args):
	isRecursive = False
	recursionDepth = 1
	url = None
	saveDest = "./data/"

	for i, arg in enumerate(args):
		if arg == '-r':
			isRecursive = True
			if "-l" not in args:
				recursionDepth = 5
		if arg == '-l':
			if "-r" in args:
				try:
					recursionDepth = int(args[i + 1])
				except (IndexError, ValueError):
					recursionDepth = -1
		if arg == '-p':
			try:
				p = Path(args[i +1])
				if p.exists() and p.is_dir():
					saveDest = args[i + 1]
				else:
					raise ValueError
			except (IndexError, ValueError):
				saveDest = ""
			


	return (isRecursive, recursionDepth, url, saveDest)


if __name__ == '__main__':
	isRecursive, recursionDepth, url, saveDest = main(sys.argv[1:])

	print(f"Is recursive: {isRecursive}")
	print(f"Recursion depth: {recursionDepth}")
	print(f"URL: {url}")
	print(f"Save destination: {saveDest}")
