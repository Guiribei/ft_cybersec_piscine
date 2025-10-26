from src.exceptions import (
    ArgumentError,
    MissingUrlError,
    MissingArgumentError,
    BadArgumentError,
)
from src.Options import Options

import sys
from pathlib import Path


def parse_args(args) -> Options:
    options = Options()

    # Get URL
    if not args:
        raise MissingUrlError("No URL provided")
    options.url = args.pop()

    stack = args[::-1]  # Reverse the args and treat as a LIFO stack
    parsed_tokens = set()  # Set of already parsed tokens to avoid duplicates

    while stack:
        token = stack.pop()
        if token == "-l" and "-l" not in parsed_tokens:
            if not stack:
                options.recursion_depth = 5
            else:
                try:
                    options.recursion_depth = int(stack[-1])
                    if options.recursion_depth <= 0 or options.recursion_depth > 6:
                        # Value is a valid integer but semantically incorrect
                        raise BadArgumentError("Recursion depth must be between 1 and 6")
                    stack.pop()
                except ValueError:
                    options.recursion_depth = 5
                parsed_tokens.add("-l")

        elif token == "-p" and "-p" not in parsed_tokens:
            if not stack:
                raise MissingArgumentError("Missing value after -p flag")
            path = stack.pop()
            p = Path(path)
            if p.exists() and p.is_dir():
                options.save_dest = path
            else:
                raise BadArgumentError("Provided path is not a valid directory")
            parsed_tokens.add("-p")

        elif token == "-r" and "-r" not in parsed_tokens:
            options.is_recursive = True
            if "-l" not in parsed_tokens:
                options.recursion_depth = 5
            parsed_tokens.add("-r")

        else:
            raise ArgumentError(f"Unknown argument: {token}")

    return options


if __name__ == "__main__":
    try:
        options = parse_args(sys.argv[1:])
    except (ArgumentError, MissingUrlError, MissingArgumentError, BadArgumentError) as e:
        print(f"Error: {e} ❌")
        print("Usage: ./spider [-rlp] URL")
        sys.exit(1)  # exit gracefully with error code

    print(f"----------------------------------")
    print(f"Is recursive: {options.is_recursive}")
    print(f"Recursion depth: {options.recursion_depth}")
    print(f"Save destination: {options.save_dest}")
    print(f"URL: {options.url}")
    print(f"----------------------------------")
