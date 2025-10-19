from src.Options import Options

from typing import List, Optional, Type


class TestCase:
    def __init__(
        self,
        name: str,
        args: List[str],
        should_raise_exception: bool,
        expected_result: Optional[Options] = None,
        expected_exception: Optional[Type[Exception]] = None,
    ):
        self.name = name
        self.args = args
        self.should_raise_exception = should_raise_exception
        self.expected_result = expected_result
        self.expected_exception = expected_exception

    def __repr__(self):
        return (
            f"<TestCase name={self.name!r} "
            f"args={self.args!r} "
            f"should_raise_exception={self.should_raise_exception} "
            f"expected_result={self.expected_result!r} "
            f"expected_exception={getattr(self.expected_exception, '__name__', None)}>"
        )
