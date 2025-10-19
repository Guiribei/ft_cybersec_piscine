from spider import (
    parse_args,
    DEFAULT_DIR,
    ArgumentError,
    MissingArgumentError,
    MissingUrlError,
    BadArgumentError,
)


# Text Formatting
BOLD = "\033[1m"
RED = "\033[31m"
GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
RESET = "\033[0m"

# TEST SUITE
TEST_DIR_PATH = "test/path"
TEST_URL = "http://example.com"

failed_tests_count = 0

# Run tests
print(f"{BOLD}RUNNING TEST SUITE...{RESET}")
#######################################################################################
# POSITIVE TESTS
positive_tests = [
    {
        "name": "Single URL only",
        "args": [TEST_URL],
        "should_raise_exception": False,
        "expected_result": (False, 1, TEST_URL, DEFAULT_DIR),
        "expected_exception": None,
    },
    {
        "name": "Recursive with default depth",
        "args": ["-r", TEST_URL],
        "should_raise_exception": False,
        "expected_result": (True, 5, TEST_URL, DEFAULT_DIR),
        "expected_exception": None,
    },
    {
        "name": "Recursive with specified depth (3)",
        "args": ["-r", "-l", "3", TEST_URL],
        "should_raise_exception": False,
        "expected_result": (True, 3, TEST_URL, DEFAULT_DIR),
        "expected_exception": None,
    },
    {
        "name": "Specified depth only",
        "args": ["-l", "3", TEST_URL],
        "should_raise_exception": False,
        "expected_result": (False, 3, TEST_URL, DEFAULT_DIR),
        "expected_exception": None,
    },
    {
        "name": "Specified path only",
        "args": ["-p", "./test/path/", TEST_URL],
        "should_raise_exception": False,
        "expected_result": (False, 1, TEST_URL, "./test/path/"),
        "expected_exception": None,
    },
    {
        "name": "Specified path (.)",
        "args": ["-p", ".", TEST_URL],
        "should_raise_exception": False,
        "expected_result": (False, 1, TEST_URL, "."),
        "expected_exception": None,
    },
    {
        "name": "Specified path (..)",
        "args": ["-p", "..", TEST_URL],
        "should_raise_exception": False,
        "expected_result": (False, 1, TEST_URL, ".."),
        "expected_exception": None,
    },
    {
        "name": "Recursive with specified depth (6) - different arg order",
        "args": ["-l", 6, "-r", TEST_URL],
        "should_raise_exception": False,
        "expected_result": (True, 6, TEST_URL, DEFAULT_DIR),
        "expected_exception": None,
    },
    {
        "name": "Recursive with specified depth (1)",
        "args": ["-r", "-l", 1, TEST_URL],
        "should_raise_exception": False,
        "expected_result": (True, 1, TEST_URL, DEFAULT_DIR),
        "expected_exception": None,
    },
    {
        "name": "Recursive with specified depth (1) - different arg order",
        "args": ["-l", 1, "-r", TEST_URL],
        "should_raise_exception": False,
        "expected_result": (True, 1, TEST_URL, DEFAULT_DIR),
        "expected_exception": None,
    },
    {
        "name": "Recursive with specified path",
        "args": ["-r", "-p", TEST_DIR_PATH, TEST_URL],
        "should_raise_exception": False,
        "expected_result": (True, 5, TEST_URL, TEST_DIR_PATH),
        "expected_exception": None,
    },
    {
        "name": "Recursive with specified path - different arg order",
        "args": ["-p", TEST_DIR_PATH, "-r", TEST_URL],
        "should_raise_exception": False,
        "expected_result": (True, 5, TEST_URL, TEST_DIR_PATH),
        "expected_exception": None,
    },
    {
        "name": "Specified path and depth",
        "args": ["-p", TEST_DIR_PATH, "-l", 10, TEST_URL],
        "should_raise_exception": False,
        "expected_result": (False, 10, TEST_URL, TEST_DIR_PATH),
        "expected_exception": None,
    },
    {
        "name": "All options specified",
        "args": ["-r", "-p", TEST_DIR_PATH, "-l", 10, TEST_URL],
        "should_raise_exception": False,
        "expected_result": (True, 10, TEST_URL, TEST_DIR_PATH),
        "expected_exception": None,
    },
]

for i, case in enumerate(positive_tests, 1):
    try:
        actual = parse_args(case["args"])
        assert (
            actual == case["expected_result"]
        ), f"Expected {case['expected_result']}, got {actual}"
        print(f"Test {i} - {case['name']}: {GREEN_BOLD}OK!{RESET}")
    except AssertionError as e:
        print(
            f"Test {i} - {case['name']}: {BOLD}{RED}NOK!{RESET} {type(e).__name__}: {e}"
        )
        failed_tests_count += 1
    except Exception as e:
        print(
            f"Test {i} - {case['name']}: {BOLD}{RED}NOK!{RESET} Unexpected exception: {e}"
        )
        failed_tests_count += 1

# NEGATIVE TESTS
negative_tests = [
    {
        "name": "No arguments",
        "args": [],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": MissingUrlError,
    },
    {
        "name": "Wrong argument",
        "args": ["r", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": ArgumentError,
    },
    {
        "name": "Recursive - invalid argument",
        "args": ["-r", "6", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": ArgumentError,
    },
    {
        "name": "Recursive with missing specified depth",
        "args": ["-r", "-l", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": MissingArgumentError,
    },
    {
        "name": "Recursive with missing specified depth - different arg order",
        "args": ["-l", "-r", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": BadArgumentError,
    },
    {
        "name": "Recursive with bad specified depth",
        "args": ["-r", "-l", "a", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": BadArgumentError,
    },
    {
        "name": "Recursive with invalid (too large) specified depth",
        "args": ["-r", "-l", "--zzzzzzzzxxxxhxhxsxuiashx78asxhaxuhsa9x04234", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": BadArgumentError,
    },
    {
        "name": "Specified depth only - missing argument",
        "args": ["-l", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": MissingArgumentError,
    },
    {
        "name": "Specified depth only - bad argument",
        "args": ["-l", "a", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": BadArgumentError,
    },
    {
        "name": "Specified path only - missing argument",
        "args": ["-p", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": MissingArgumentError,
    },
    {
        "name": "Specified path only - invalid directory",
        "args": ["-p", ".//////////sdf/sd/f/sdf", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": BadArgumentError,
    },
    {
        "name": "Recursive with specified depth (6) - invalid arg order",
        "args": ["-r", 6, "-l", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": ArgumentError,
    },
    {
        "name": "Recursive with specified depth (7) - invalid argument",
        "args": ["-r", 6, "-l", 7, TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": ArgumentError,
    },
    {
        "name": "Recursive with specified path - missing argument",
        "args": ["-r", "-p", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": MissingArgumentError,
    },
    {
        "name": "Specified path and depth - missing depth argument",
        "args": ["-p", TEST_DIR_PATH, "-l", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": MissingArgumentError,
    },
    {
        "name": "Recursive with negative specified depth",
        "args": ["-r", "-l", "-3", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": BadArgumentError,
    },
    {
        "name": "Recursive with specified depth equal to zero",
        "args": ["-r", "-l", "0", TEST_URL],
        "should_raise_exception": True,
        "expected_result": None,
        "expected_exception": BadArgumentError,
    },
]

for i, test in enumerate(negative_tests, 1):
    try:
        parse_args(test["args"])
        print(f"Test {i} {test['name']}: {BOLD}{RED}NOK!{RESET} Expected exception")
        failed_tests_count += 1
    except test["expected_exception"]:
        print(f"Test {i} {test['name']}: {GREEN_BOLD}OK!{RESET}")
    except Exception as e:
        print(
            f"Test {i} {test['name']}: {BOLD}{RED}NOK!{RESET} Unexpected exception: {type(e).__name__} (`{e}`); Expected: {test['expected_exception'].__name__}"
        )
        failed_tests_count += 1
#######################################################################################


# Print test results
## Header
print("\n" + "-" * 66)
print(f"{BOLD}{' TEST REPORT ':=^66}{RESET}")
print("-" * 66)


# Body
total_test_cases = len(positive_tests) + len(negative_tests)
print(f"{BOLD}TOTAL TEST CASES: {total_test_cases}{RESET}")
print(f"{BOLD}FAILED TEST CASES: {RED}{failed_tests_count}{RESET}")

# Compute passing rate safely
if total_test_cases > 0:
    passing_rate = (total_test_cases - failed_tests_count) / total_test_cases * 100
else:
    passing_rate = 0.0

# Choose color based on result
if passing_rate == 100:
    rate_color = GREEN_BOLD
elif passing_rate >= 80:
    rate_color = YELLOW_BOLD
else:
    rate_color = f"{BOLD}{RED}"

print()
print(f"{rate_color}Passing Rate: {passing_rate:.2f}%{RESET}")
print("-" * 66)
