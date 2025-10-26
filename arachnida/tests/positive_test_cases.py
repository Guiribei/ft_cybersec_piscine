from src.Options import DEFAULT_DIR, Options

from tests import TEST_URL, TEST_DIR_PATH, TestCase

positive_tests = [
    TestCase(
        name="Single URL only",
        args=[TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=False, recursion_depth=1, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with default depth",
        args=["-r", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=5, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with specified depth (3)",
        args=["-r", "-l", "3", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=3, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with missing specified depth - different arg order",
        args=["-l", "-r", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=5, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Specified depth only - missing argument",
        args=["-l", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=False, recursion_depth=5, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Specified depth only",
        args=["-l", "3", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=False, recursion_depth=3, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Specified path only",
        args=["-p", TEST_DIR_PATH, TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=False, recursion_depth=1, save_dest=TEST_DIR_PATH, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Specified path (.)",
        args=["-p", ".", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=False, recursion_depth=1, save_dest=".", url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Specified path (..)",
        args=["-p", "..", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=False, recursion_depth=1, save_dest="..", url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with missing specified depth",
        args=["-r", "-l", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=5, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with specified depth (6) - different arg order",
        args=["-l", 6, "-r", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=6, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with specified depth (1)",
        args=["-r", "-l", 1, TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=1, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with specified depth (1) - different arg order",
        args=["-l", 1, "-r", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=1, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with depth arg - depth not specified",
        args=["-r", "-l", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=5, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with depth arg - depth not specified, different arg order",
        args=["-l", "-r", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=5, save_dest=DEFAULT_DIR, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with specified path",
        args=["-r", "-p", TEST_DIR_PATH, TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=5, save_dest=TEST_DIR_PATH, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Recursive with specified path - different arg order",
        args=["-p", TEST_DIR_PATH, "-r", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=5, save_dest=TEST_DIR_PATH, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Specified path and depth",
        args=["-p", TEST_DIR_PATH, "-l", 10, TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=False,
            recursion_depth=10,
            save_dest=TEST_DIR_PATH,
            url=TEST_URL,
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Specified path and depth - different arg order",
        args=["-l", 10, "-p", TEST_DIR_PATH, TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=False,
            recursion_depth=10,
            save_dest=TEST_DIR_PATH,
            url=TEST_URL,
        ),
        expected_exception=None,
    ),
    TestCase(
        name="Specified path and depth - missing depth argument",
        args=["-p", TEST_DIR_PATH, "-l", TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=False,
            recursion_depth=5,
            save_dest=TEST_DIR_PATH,
            url=TEST_URL,
        ),
        expected_exception=None,
    ),
    TestCase(
        name="All options specified",
        args=["-r", "-l", 10, "-p", TEST_DIR_PATH, TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=10, save_dest=TEST_DIR_PATH, url=TEST_URL
        ),
        expected_exception=None,
    ),
    TestCase(
        name="All options specified - different arg order",
        args=["-r", "-p", TEST_DIR_PATH, "-l", 10, TEST_URL],
        should_raise_exception=False,
        expected_result=Options(
            is_recursive=True, recursion_depth=10, save_dest=TEST_DIR_PATH, url=TEST_URL
        ),
        expected_exception=None,
    ),
]
