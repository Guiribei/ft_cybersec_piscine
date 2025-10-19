import sys
from pathlib import Path


DEFAULT_DIR = "./data/"


class ArgumentError(Exception):
    """Raised when parse_args encounters invalid arguments."""

    pass


class MissingUrlError(Exception):
    """Raised when no URL is provided in the arguments."""

    pass


class MissingArgumentError(Exception):
    """Raised when an option is not provided with an argument."""

    pass


class BadArgumentError(Exception):
    """Raised when an option is provided an argument with the wrong type or format."""

    pass


def parse_args(args):
	# Options
	# Todo: turn this into a dict or class idk
	isRecursive = False
	recursionDepth = -42
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
					if recursionDepth <= 0:
						raise ValueError
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

	if recursionDepth == -42:
		recursionDepth = 1

	return (isRecursive, recursionDepth, url, saveDest)


if __name__ == '__main__':
	isRecursive, recursionDepth, url, saveDest = parse_args(sys.argv[1:])

	print(f"----------------------------------")
	print(f"Is recursive: {isRecursive}")
	print(f"Recursion depth: {recursionDepth}")
	print(f"URL: {url}")
	print(f"Save destination: {saveDest}")
	print(f"----------------------------------")
