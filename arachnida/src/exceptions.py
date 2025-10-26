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