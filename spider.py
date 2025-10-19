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
    # TODO: turn this into a dict or class idk
    isRecursive: bool = False
    recursionDepth: int = 1
    saveDest: str = DEFAULT_DIR
    url: str | None = None

    # Get URL
    if not args:
        raise MissingUrlError("No URL provided")
    url = args.pop()

    stack = args[::-1]  # Reverse the args and treat as a LIFO stack
    parsed_tokens = set()  # Set of already parsed tokens to avoid duplicates

    while stack:
        token = stack.pop()
        if token == "-l" and "-l" not in parsed_tokens:
            if not stack:
                # No value provided after the flag
                raise MissingArgumentError("Missing value after -l flag")

            value_str = stack.pop()
            try:
                recursionDepth = int(value_str)
            except ValueError:
                # Value exists but is not a valid integer
                raise BadArgumentError(f"Invalid value for -l flag: {value_str!r}")

            if recursionDepth <= 0:
                # Value is a valid integer but semantically incorrect
                raise BadArgumentError("Recursion depth must be positive")

            parsed_tokens.add("-l")

        elif token == "-p" and "-p" not in parsed_tokens:
            if not stack:
                raise MissingArgumentError("Missing value after -p flag")
            path = stack.pop()
            p = Path(path)
            if p.exists() and p.is_dir():
                saveDest = path
            else:
                raise BadArgumentError("Provided path is not a valid directory")
            parsed_tokens.add("-p")

        elif token == "-r" and "-r" not in parsed_tokens:
            isRecursive = True
            if "-l" not in parsed_tokens:
                recursionDepth = 5
            parsed_tokens.add("-r")

        else:
            raise ArgumentError(f"Unknown argument: {token}")

    return (isRecursive, recursionDepth, url, saveDest)


if __name__ == "__main__":
    isRecursive, recursionDepth, url, saveDest = parse_args(sys.argv[1:])

    print(f"----------------------------------")
    print(f"Is recursive: {isRecursive}")
    print(f"Recursion depth: {recursionDepth}")
    print(f"URL: {url}")
    print(f"Save destination: {saveDest}")
    print(f"----------------------------------")
